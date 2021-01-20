import ast
import json

from flask import render_template, request, redirect
from flask_classful import FlaskView, route

from db_actions import *


class SqliteView(FlaskView):
    table_name = "batch"

    def index(self):
        with open("parameters.json") as file:
            data = json.load(file)
            database = SQLiteDBManagement(path_to_first_sqlite_db=data["sqlite_path"],
                                          path_to_second_sqlite_db='SQLiteDBs/trigger.db')
        return render_template("db_view.html", table=database.get_table("batch"),
                               column_names=database.get_table_columns("batch"))

    @route("delete_batch_id_array", methods=["POST"])
    def delete_from_table_by_id(self):
        with open("parameters.json") as file:
            data = json.load(file)
            database = SQLiteDBManagement(path_to_first_sqlite_db=data["sqlite_path"])
        database.delete(tablename=self.table_name, column="batch_inspectionid",
                        condition=ast.literal_eval(request.form.get('data')))
        return redirect("/postgres")

    @route("delete_batch_name_array", methods=["POST"])
    def delete_from_table_by_name(self):
        with open("parameters.json") as file:
            data = json.load(file)
            database = SQLiteDBManagement(path_to_first_sqlite_db=data["sqlite_path"])
        database.delete(tablename=self.table_name, column="batchname",
                        condition=ast.literal_eval(request.form.get('data')))
        return redirect("/postgres")

    def delete_from_table_between_ids(self):
        return redirect("/postgres")
