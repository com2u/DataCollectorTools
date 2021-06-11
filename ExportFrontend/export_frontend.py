from flask import Blueprint, request, url_for, render_template, redirect
from db_actions import PostgersqlDBManagement
import json

export = Blueprint(
    'export', __name__, url_prefix="/export", template_folder='templates')

@export.route('/')
def export_index():
    return render_template("export_index.html")


@export.route('/alltables')
def alltables():
    with open("parameters.json") as file:
        data = json.load(file)
        database = PostgersqlDBManagement(username=data["postgres_user"], password=data["postgres_pw"],
                                          url=data["postgres_url"], dbname=data["postgres_db"])
    alltables = []
    table_names = database.get_view_names()
    table_names.extend(database.get_table_names())
    for i in table_names:
        alltables.append({
            "table_name": str(i)
        })
    return render_template("view.html", alltables=alltables)


@export.route('/filter', methods=["GET", "POST"])
def page_filter():
    if request.method == "POST":
        return redirect(url_for("page_view"), code=307)
    return render_template("filter.html")


@export.route('/view', methods=["GET"])
def page_view():
    with open("parameters.json") as file:
        data = json.load(file)
        database = PostgersqlDBManagement(username=data["postgres_user"], password=data["postgres_pw"],
                                          url=data["postgres_url"], dbname=data["postgres_db"])
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
def page_process():
    return render_template("processing.html")