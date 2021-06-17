import py7zr
import json
import os
import shutil
import time
import subprocess
import pandas as pd

from flask import Blueprint, jsonify, request, send_file, after_this_request
from db_actions import PostgersqlDBManagement
from io import BytesIO
from pathlib import Path
from os.path import basename

export_interface = Blueprint(
    'export_interface', __name__, url_prefix="/export_interface")


def get_db_instance():
    with open("parameters.json") as file:
        data = json.load(file)
        database = PostgersqlDBManagement(username=data["postgres_user"], password=data["postgres_pw"],
                                          url=data["postgres_url"], dbname=data["postgres_db"])
    return database


def to_dict(row):
    if row is None:
        return None
    rtn_dict = dict()
    keys = row.__table__.columns.keys()
    for key in keys:
        rtn_dict[key] = getattr(row, key)
    return rtn_dict


@export_interface.route("/folder/csv")
def export_folder_csv():
    database = get_db_instance()
    id = time.strftime("%Y%m%d-%H%M%S")
    with open("parameters.json") as file:
        data = json.load(file)
    folder_name = Path(str(data["export_path"]), id)
    folder_name.mkdir(parents=True, exist_ok=True)

    # creating a csv file for every table
    for table_name in database.get_view_names():
        data_list = [dict(row) for row in database.get_table(
            table_name, filter=request.values.to_dict())]
        if len(data_list) > 0:
            df = pd.DataFrame(data_list)
            df.columns = database.get_table_columns(table_name)
            df.to_csv(os.path.join(folder_name, f"{table_name}.csv"))
    return jsonify(export_folder=str(folder_name))


@export_interface.route("/folder/excel")
def export_folder_excel():
    database = get_db_instance()
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    for table_name in database.get_view_names():
        data_list = [dict(row) for row in database.get_table(
            table_name, filter=request.values.to_dict())]
        if len(data_list) > 0:
            df = pd.DataFrame(data_list)
            df.columns = database.get_table_columns(table_name)
            df.to_excel(writer, sheet_name=str(table_name))
    writer.close()
    output.seek(0)

    id = time.strftime("%Y%m%d-%H%M%S")
    with open("parameters.json") as file:
        data = json.load(file)
    folder_name = Path(str(data["export_path"]), id)
    folder_name.mkdir(parents=True, exist_ok=True)
    with open(f"{folder_name}\\Tables.xlsx", "wb") as outfile:
        outfile.write(output.getbuffer())
    return jsonify(export_folder=str(folder_name))


@export_interface.route("/folder/pictures")
def export_folder_pictures():
    database = get_db_instance()
    id = time.strftime("%Y%m%d-%H%M%S")
    with open("parameters.json") as file:
        data = json.load(file)
    folder_name = Path(str(data["export_path"]), id)
    folder_name.mkdir(parents=True, exist_ok=True)
    pathes_to_pictures = database.get_table_column_values(
        "trigger_image_links", "image1")
    if len(pathes_to_pictures) > 0:
        for file in pathes_to_pictures:
            shutil.copy(file, str(folder_name))
        return jsonify(export_folder=str(folder_name))
    return ""


@export_interface.route("/download/csv")
def download_csv():
    database = get_db_instance()
    memory_file = BytesIO()
    with py7zr.SevenZipFile(memory_file, 'w') as zf:
        for table_name in database.get_view_names():
            data_list = [dict(row) for row in database.get_table(
                table_name, filter=request.values.to_dict())]
            if len(data_list) > 0:
                df = pd.DataFrame(data_list)
                df.columns = database.get_table_columns(table_name)
                zf.writestr(df.to_csv().encode(), arcname=f"{table_name}.csv")     
    memory_file.seek(0)
    return send_file(memory_file, attachment_filename="testing.7z", as_attachment=True)


@export_interface.route("/download/excel")
def download_excel():
    database = get_db_instance()
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    for table_name in database.get_view_names():
        data_list = [dict(row) for row in database.get_table(
            table_name, filter=request.values.to_dict())]
        if len(data_list) > 0:
            df = pd.DataFrame(data_list)
            df.columns = database.get_table_columns(table_name)
            df.to_excel(writer, sheet_name=str(table_name))
    writer.close()
    output.seek(0)
    return send_file(output, attachment_filename="testing.xlsx", as_attachment=True)


@export_interface.route("/download/pictures")
def download_pictures():
    database = get_db_instance()
    memory_file = BytesIO()
    pathes_to_pictures = database.get_table_column_values(
        "trigger_image_links", "image1")
    if len(pathes_to_pictures) > 0:
        with py7zr.SevenZipFile(memory_file, 'w') as zf:
            for picture in pathes_to_pictures:
                zf.write(picture, basename(picture))
        memory_file.seek(0)
        return send_file(memory_file, attachment_filename="pictures_testing.7z", as_attachment=True)
    return ""

@export_interface.route("/dump")
def dump_all():
    with open("parameters.json") as file:
        data = json.load(file)
    command = ["pg_dump", f'--dbname=postgresql://{data["postgres_user"]}:{data["postgres_pw"]}@{data["postgres_url"]}:5432/{data["postgres_db"]}', '--format=c']
    output = subprocess.Popen(command, stdout=subprocess.PIPE)
    database_dump = output.stdout.read()
    memory_file = BytesIO()
    with py7zr.SevenZipFile(memory_file, "w", password="Pzma9T2nvz04KK1A9CU7") as zf:
        zf.writestr(arcname="dump.sql", data=database_dump)
    memory_file.seek(0)
    return send_file(memory_file, attachment_filename="dump.7z", as_attachment=True)