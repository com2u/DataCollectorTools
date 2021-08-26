import py7zr
import json
import os
import shutil
import time
import subprocess
import uuid
import pandas as pd
import db_actions

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
            downloadData = BytesIO()
            if 'downloadExcel' in params['check']:
                downloadData = get_excel(params, downloadData)
            if 'downloadCSV' in params['check']:
                downloadData = get_csv(params, downloadData)
            if 'downloadImages' in params['check']:
                downloadData = get_pictures(params, downloadData)
            if 'downloadDatabaseDump' in params['check']:
                downloadData = get_dump(params, downloadData)
        if 'export' in params['check']:
            exportData = BytesIO()
            if 'exportExcel' in params['check']:
                exportData = get_excel(params, exportData)
            if 'exportCSV' in params['check']:
                exportData = get_csv(params, exportData)
            if 'exportImages' in params['check']:
                exportData = get_pictures(params, exportData)
            if 'exportDatabaseDump' in params['check']:
                exportData = get_dump(params, exportData)
        if 'delete' in params:
            if 'deleteImages' in params:
                test = 'test'
    return jsonify(params)


def get_csv(filter, memory_file=BytesIO()):
    database = db_actions.get_postgres_instance()
    with py7zr.SevenZipFile(memory_file, 'w') as zf:
        for table_name in database.get_view_names():
            data_list = [dict(row) for row in database.get_table(
                table_name, filter=filter)]
            if len(data_list) > 0:
                df = pd.DataFrame(data_list)
                df.columns = database.get_table_columns(table_name)
                zf.writestr(df.to_csv().encode(), arcname=f"{table_name}.csv")
    return memory_file


def get_excel(filter, memory_file=BytesIO()):
    database = db_actions.get_postgres_instance()
    writer = pd.ExcelWriter(memory_file, engine='xlsxwriter')
    for table_name in database.get_view_names():
        data_list = [dict(row) for row in database.get_table(
            table_name, filter=filter)]
        if len(data_list) > 0:
            df = pd.DataFrame(data_list)
            df.columns = database.get_table_columns(table_name)
            df.to_excel(writer, sheet_name=str(table_name))
    writer.close()
    return memory_file


def get_pictures(filter, memory_file=BytesIO()):
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
            memory_file.write(fh.read())
        # removing temporary files
        os.remove(zip_uuid + ".7z")
        os.remove(zip_uuid + ".txt")
        return memory_file
    return memory_file


def get_dump(memory_file=BytesIO()):
    with py7zr.SevenZipFile(memory_file, 'w', password="Pzma9T2nvz04KK1A9CU7") as zf:
        with open("parameters.json") as file:
            data = json.load(file)
        command = [
            "pg_dump", f'--dbname=postgresql://{data["postgres_user"]}:{data["postgres_pw"]}@{data["postgres_url"]}:5432/{data["postgres_db"]}', '--format=c']
        output = subprocess.Popen(command, stdout=subprocess.PIPE)
        database_dump = output.stdout.read()
        zf.writestr(data=database_dump, arcname="dump.backup")
    return memory_file


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
