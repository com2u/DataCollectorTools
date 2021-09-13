from flask import Blueprint, jsonify, request, render_template
from db_actions import PostgersqlDBManagement
import json
import os
import sys

from Oidc_Decorators import oidc

config_interface = Blueprint(
    'config_interface', __name__, url_prefix="/config_interface", template_folder='templates')


@config_interface.route('/config')
@oidc.require_login
def page_config():
    return render_template("config.html")


@config_interface.route("/", methods=["GET"])
@oidc.require_login
def get_config():
    json_data = {
        "postgres_url": os.getenv("DATABASE_ADDR"),
        "postgres_user": os.getenv("DATABASE_USER"),
        "postgres_db": os.getenv("DATABASE_NAME_VISION"),
        "limit_table_length": os.getenv("TABLE_LENGTH_LIMIT"),
        "export_path": os.getenv("EXPORT_PATH")
    }
    return jsonify(json_data)


@config_interface.route("/", methods=["POST"])
@oidc.require_login
def post_config():
    req = request.form
    accepted_parameters = ["postgres_url",
                           "postgres_user",
                           "postgres_pw",
                           "postgres_db",
                           "limit_table_length",
                           "export_path"]
    for parameter in accepted_parameters:
        if parameter in req:
            if req[parameter] != "":
                if parameter == 'postgres_url':
                    os.environ["DATABASE_ADDR"] = str(req[parameter])
                elif parameter == 'postgres_user':
                    os.environ["DATABASE_USER"] = str(req[parameter])
                elif parameter == 'postgres_pw':
                    os.environ["DATABASE_PASSWORD"] = str(req[parameter])
                elif parameter == 'postgres_db':
                    os.environ["DATABASE_NAME_VISION"] = str(req[parameter])
                elif parameter == 'limit_table_length':
                    os.environ["TABLE_LENGTH_LIMIT"] = str(req[parameter])
                elif parameter == 'export_path':
                    os.environ["EXPORT_PATH"] = str(req[parameter])
    return jsonify(success=True)


@config_interface.route("/reset", methods=["POST"])
@oidc.require_login
def reset_config():
    os.environ["DATABASE_ADDR"] = str(os.getenv("DEFAULT_DATABASE_ADDR"))
    os.environ["DATABASE_USER"] = str(os.getenv("DEFAULT_DATABASE_USER"))
    os.environ["DATABASE_PASSWORD"] = str(os.getenv("DEFAULT_DATABASE_PASSWORD"))
    os.environ["DATABASE_NAME_VISION"] = str(os.getenv("DEFAULT_DATABASE_NAME_VISION"))
    os.environ["TABLE_LENGTH_LIMIT"] = str(os.getenv("DEFAULT_TABLE_LENGTH_LIMIT"))
    os.environ["EXPORT_PATH"] = str(os.getenv("DEFAULT_EXPORT_PATH"))
    return jsonify(success=True)
