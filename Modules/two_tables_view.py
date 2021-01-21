import json

from flask import render_template
from flask_classful import FlaskView

from db_actions import PostgersqlDBManagement


class TwotablesView(FlaskView):
    def index(self):
        with open("parameters.json") as file:
            data = json.load(file)
        database = PostgersqlDBManagement(username=data["postgres_user"], password=data["postgres_pw"],
                                          url=data["postgres_url"], dbname=data["postgres_db"])
        table_name = "batch"
        return render_template("two_tables.html", table_name=table_name,
                               column_names=database.get_table_columns(table_name),
                               table=database.get_table(table_name))
