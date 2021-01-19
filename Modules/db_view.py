import ast
import json

from flask import render_template, request, redirect
from flask_classful import FlaskView, route

from db_actions import *


class PostgresView(FlaskView):
    table_name = "batch"

    def index(self):
        postgres = PostgersqlDBManagement(username="postgres", password="LX8FSRdT6r6f7UEe", url="localhost",
                                          dbname="test1234")
        return render_template("db_view.html", table=postgres.get_table("batch"),
                               column_names=postgres.get_table_columns("batch"))

    @route("delete_batch_id_array", methods=["POST"])
    def delete_from_table_by_id(self):
        with open("parameters.json") as file:
            data = json.load(file)
            database = PostgersqlDBManagement(username=data["postgres_user"], password=data["postgres_pw"],
                                              url=data["postgres_url"], dbname=data["postgres_db"])
        database.delete(tablename=self.table_name, column="batch_inspectionid",
                        condition=ast.literal_eval(request.form.get('data')))
        return redirect("/postgres")

    @route("delete_batch_name_array", methods=["POST"])
    def delete_from_table_by_name(self):
        with open("parameters.json") as file:
            data = json.load(file)
            database = PostgersqlDBManagement(username=data["postgres_user"], password=data["postgres_pw"],
                                              url=data["postgres_url"], dbname=data["postgres_db"])
        database.delete(tablename=self.table_name, column="batchname",
                        condition=ast.literal_eval(request.form.get('data')))
        return redirect("/postgres")

    def delete_from_table_between_ids(self):
        return redirect("/postgres")
