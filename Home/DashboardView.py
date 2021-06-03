import ast
import json
from Oidc_Decorators import Decorators
from db_actions import PostgersqlDBManagement, SQLiteDBManagement
from Oidc_Decorators.Decorators import require_keycloak_role
from flask import Blueprint, render_template, request
from flask import Blueprint, render_template, redirect, url_for, flash, session

from Oidc_Decorators import oidc

dash = Blueprint('dash', __name__,  static_folder='/static', static_url_path="/pages-static",
                 template_folder='templates')

@dash.route('/home/', methods=['POST', 'GET'])
@oidc.require_login
def dashboard():
    if oidc.user_loggedin:
        return render_template('homepage.html')
      
    return redirect(url_for('start.Startscreen'))


@dash.route('/home/Postgres', methods=["GET", "POST"])
@oidc.require_login
@require_keycloak_role(["User", "Admin"])
def page_postgres():
    table_name = 'batch'
    with open("parameters.json") as file:
        data = json.load(file)
        database = PostgersqlDBManagement(username=data["postgres_user"], password=data["postgres_pw"],
                                          url=data["postgres_url"], dbname=data["postgres_db"])
    return render_template("table_view.html", table_name=table_name, db_name="Postgres",
                           column_names=database.get_table_columns(table_name),
                           table=database.get_table(table_name))


@dash.route("/home/Postgres/delete_batch_id_array", methods=["POST"])
@oidc.require_login
@require_keycloak_role(["User", "Admin"])
def delete_from_table_by_id_postgres():
    table_name = 'batch'
    with open("parameters.json") as file:
        data = json.load(file)
        database = PostgersqlDBManagement(username=data["postgres_user"], password=data["postgres_pw"],
                                          url=data["postgres_url"], dbname=data["postgres_db"])
    database.delete(tablename=table_name, column="batch_inspectionid",
                    condition=ast.literal_eval(request.form.get('data')))
    return "True"


@dash.route("/home/Postgres/delete_batch_name_array", methods=["POST"])
@oidc.require_login
@require_keycloak_role(["User", "Admin"])
def delete_from_table_by_name_postgres():
    table_name = 'batch'
    with open("parameters.json") as file:
        data = json.load(file)
        database = PostgersqlDBManagement(username=data["postgres_user"], password=data["postgres_pw"],
                                          url=data["postgres_url"], dbname=data["postgres_db"])
    database.delete(tablename=table_name, column="batchname",
                    condition=ast.literal_eval(request.form.get('data')))
    return "True"


@dash.route('/home/SQLite', methods=["GET", "POST"])
@oidc.require_login
@require_keycloak_role(["User", "Admin"])
def page_sqlite():
    table_name = 'batch'
    with open("parameters.json") as file:
        data = json.load(file)
        database = SQLiteDBManagement(path_to_sqlite_db=data["sqlite_path"])
    return render_template("table_view.html", table_name=table_name, db_name="SQLite",
                           column_names=database.get_table_columns(table_name),
                           table=database.get_table(table_name))


@dash.route("/home/SQLite/delete_batch_id_array", methods=["POST"])
@oidc.require_login
@require_keycloak_role(["User", "Admin"])
def delete_from_table_by_id_sqlite():
    table_name = 'batch'
    with open("parameters.json") as file:
        data = json.load(file)
        database = SQLiteDBManagement(path_to_sqlite_db=data["sqlite_path"])
    database.delete(tablename=table_name, column="batch_inspectionid",
                    condition=ast.literal_eval(request.form.get('data')))
    return "True"


@dash.route("/home/SQLite/delete_batch_name_array", methods=["POST"])
@oidc.require_login
@require_keycloak_role(["User", "Admin"])
def delete_from_table_by_name_sqlite():
    table_name = 'batch'
    with open("parameters.json") as file:
        data = json.load(file)
        database = SQLiteDBManagement(path_to_sqlite_db=data["sqlite_path"])
    database.delete(tablename=table_name, column="batchname",
                    condition=ast.literal_eval(request.form.get('data')))
    return "True"
