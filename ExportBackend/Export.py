import py7zr
import json
import os
import subprocess
import uuid
import pandas as pd
import db_actions
from datetime import datetime

from flask import Blueprint, jsonify, request, send_file, after_this_request
from io import BytesIO
from pathlib import Path
from os.path import basename
from Oidc_Decorators import oidc

process_interface = Blueprint(
    'export_interface', __name__, url_prefix="/export_interface")


@process_interface.route("/", methods=["GET"])
def process():
    params = request.values.to_dict(flat=False)
    if 'check' in params:
        if 'download' in params['check']:
            downloadFile = BytesIO()
            with py7zr.SevenZipFile(downloadFile, 'w') as downloadData:
                if 'downloadExcel' in params['check']:
                    downloadData = get_excel(params, downloadData)
                if 'downloadCSV' in params['check']:
                    downloadData = get_csv(params, downloadData)
                if 'downloadImages' in params['check']:
                    downloadData = get_pictures(params, downloadData)
            downloadFile.seek(0)
            if 'downloadDatabaseDump' in params['check']:
                with py7zr.SevenZipFile(downloadFile, 'a', password="Pzma9T2nvz04KK1A9CU7") as downloadData:
                    downloadData = get_dump(downloadData)
                downloadFile.seek(0)
        if 'export' in params['check']:
            exportFile = BytesIO()
            with py7zr.SevenZipFile(exportFile, 'w') as exportData:
                if 'exportExcel' in params['check']:
                    exportData = get_excel(params, exportData)
                if 'exportCSV' in params['check']:
                    exportData = get_csv(params, exportData)
                if 'exportImages' in params['check']:
                    exportData = get_pictures(params, exportData)
            exportFile.seek(0)
            if 'exportDatabaseDump' in params['check']:
                with py7zr.SevenZipFile(exportFile, 'a', password="Pzma9T2nvz04KK1A9CU7") as exportData:
                    exportData = get_dump(exportData)
                exportFile.seek(0)

            #saving File in Network share
            with open("parameters.json") as file:
                data = json.load(file)
            exportFileName = Path(data["export_path"], "Export_" + datetime.now().strftime("%Y-%m-%dT%H_%M_%S_%f") + ".7z")
            exportFileName.write_bytes(exportFile.getbuffer())

        
        if 'delete' in params['check']:
            if 'deleteImages' in params['check']:
                if 'deleteData' in params['check']:
                    delete_data_result = delete_db(params)
                delete_pictures_result = delete_db(params)
    return send_file(downloadFile, attachment_filename='download.7z', as_attachment=True)


def get_csv(filter, zipfile):
    database = db_actions.get_postgres_instance()
    for table_name in database.get_view_names():
        data_list = [dict(row) for row in database.get_table(
            table_name, filter=filter)]
        if len(data_list) > 0:
            df = pd.DataFrame(data_list)
            df.columns = database.get_table_columns(table_name)
            zipfile.writestr(df.to_csv().encode(),
                             arcname=f"csv/{table_name}.csv")
    return zipfile


def get_excel(filter, zipfile):
    excel_file = BytesIO()
    database = db_actions.get_postgres_instance()
    writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
    for table_name in database.get_view_names():
        data_list = [dict(row) for row in database.get_table(
            table_name, filter=filter)]
        if len(data_list) > 0:
            df = pd.DataFrame(data_list)
            df.columns = database.get_table_columns(table_name)
            df.to_excel(writer, sheet_name=str(table_name))
    writer.close()
    excel_file.seek(0)
    zipfile.writestr(excel_file.read(), arcname="tables.xlsx")
    return zipfile


def get_pictures(filter, zipfile):
    database = db_actions.get_postgres_instance()
    pathes_to_pictures = database.get_table_column_values(
        "triggerview", "image1_link", filter=filter)
    if len(pathes_to_pictures) > 0:
        zip_uuid = f"{str(uuid.uuid4())}"
        with open(zip_uuid + '.txt', "w") as file:
            for picture in pathes_to_pictures:
                file.write(picture + "\n")
        subprocess.run(["7z", "a", "-spf", "-t7z", "-m0=LZMA2:d64k:fb32", "-ms=8m", "-mmt=32",
                       "-mx=1", zip_uuid + ".7z", "@" + zip_uuid + ".txt"], stdout=subprocess.PIPE)
        with open(zip_uuid + ".7z", 'rb') as fh:
            zipfile.writestr(fh.read(), arcname="images.7z")
        # removing temporary files
        os.remove(zip_uuid + ".7z")
        os.remove(zip_uuid + ".txt")
        return zipfile
    return zipfile


def get_dump(zipfile):
    with open("parameters.json") as file:
        data = json.load(file)
    command = [
        "pg_dump", f'--dbname=postgresql://{data["postgres_user"]}:{data["postgres_pw"]}@{data["postgres_url"]}:5432/{data["postgres_db"]}', '--format=c']
    output = subprocess.Popen(command, stdout=subprocess.PIPE)
    database_dump = output.stdout.read()
    zipfile.writestr(data=database_dump, arcname="dump/dump.backup")
    return zipfile


def delete_db(filter):
    database = db_actions.get_postgres_instance()
    return jsonify(database.delete_vision(filter=filter))


def delete_pictures(filter):
    database = db_actions.get_postgres_instance()
    pathes_to_pictures = database.get_table_column_values(
        "trigger_image_links", "image1", filter=filter)
    missing_files = []
    deleted_files = []
    if len(pathes_to_pictures) > 0:
        for picture in pathes_to_pictures:
            picture = Path(picture)
            if picture.exists():
                picture.unlink()
                deleted_files.append(picture)
            else:
                missing_files.append(picture)

        return jsonify(success=True, deleted_files=len(deleted_files), missing_files=len(missing_files))
    return jsonify(success=False)
