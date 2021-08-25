from flask import Blueprint, jsonify, request
import db_actions
import base64

table_interface = Blueprint(
    'table_interface', __name__, url_prefix="/table_interface")


@table_interface.route("/")
def get_table_names():
    database = db_actions.get_postgres_instance()
    table_names = [*database.get_table_names()]
    return jsonify(columns=table_names)


@table_interface.route("/columns/<table_name>", methods=["GET"])
def get_table_columns(table_name):
    database = db_actions.get_postgres_instance()
    return jsonify({"columns": [*database.get_table_columns(table_name)]})


@table_interface.route("/column/<table_name>/<column_name>", methods=["GET"])
def get_column_content(table_name, column_name):
    database = db_actions.get_postgres_instance()
    return jsonify(database.get_table_column_values(table_name, column_name, filter=request.values.to_dict(flat=False)))



@table_interface.route("/rows/<table_name>", methods=["GET", "DELETE"])
def get_table_rows(table_name):
    if request.method == "GET":
        database = db_actions.get_postgres_instance()
        return jsonify({"data": [dict(row) for row in database.get_table(table_name, filter=request.values.to_dict(flat=False))]})
    if request.method == "DELETE":
        database = db_actions.get_postgres_instance()
        response = database.delete_from_table(
            table_name, filter=request.values.to_dict(flat=False))
        return jsonify(response)

@table_interface.route("/count/<table_name>", methods=["GET"])
def get_table_length(table_name):
    database = db_actions.get_postgres_instance()
    return jsonify({"table_name": table_name, "length":database.get_dataset_count(table_name, filter=request.values.to_dict(flat=False))})

@table_interface.route("/base64image", methods=["GET"])
def get_base64_images():
    database = db_actions.get_postgres_instance()
    image_paths = database.get_table_column_values("triggerview", "image1_link", filter=request.values.to_dict(flat=False))
    pictures = []
    for path in image_paths:
        with open(path, "rb") as image_file:
            image = base64.b64encode(image_file.read()).decode("utf-8")
            pictures.append({"path": path, "image":image})
    return jsonify({"data": pictures})

@table_interface.route("/table/<table_name>", methods=["GET"])
def get_table(table_name):
    return get_table_columns(table_name).get_json() | get_table_rows(table_name).get_json()
