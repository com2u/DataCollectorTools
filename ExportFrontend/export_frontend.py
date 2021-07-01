from flask import Blueprint, request, url_for, render_template, redirect
from db_actions import get_postgres_instance
import json

from Oidc_Decorators import oidc

export = Blueprint(
    'export', __name__, url_prefix="/export", template_folder='templates')

@export.route('/')
@oidc.require_login
def export_index():
    return render_template("export_index.html")


@export.route('/alltables')
@oidc.require_login
def alltables():
    database = get_postgres_instance()
    alltables = []
    table_names = database.get_view_names()
    table_names.extend(database.get_table_names())
    for i in table_names:
        alltables.append({
            "table_name": str(i)
        })
    return render_template("view.html", alltables=alltables)


@export.route('/filter', methods=["GET", "POST"])
@oidc.require_login
def page_filter():
    if request.method == "POST":
        return redirect(url_for("page_view"), code=307)
    return render_template("filter.html")


@export.route('/view', methods=["GET"])
@oidc.require_login
def page_view():
    database = get_postgres_instance()
    req = request.values.to_dict(flat=False)
    alltables = []
    table_names = database.get_view_names()
    for table_name in table_names:
        alltables.append({
            "table_name": str(table_name),
            "parameters": req
        })
    return render_template("view.html", alltables=alltables)


@export.route('/process', methods=["GET", "POST"])
@oidc.require_login
def page_process():
    return render_template("processing.html")
