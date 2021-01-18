from flask import render_template
from flask_classful import FlaskView

from db_actions import *


class PostgresView(FlaskView):
    def index(self):
        postgres = PostgersqlDBManagement(username="postgres", password="LX8FSRdT6r6f7UEe", url="localhost",
                                          dbname="test1234")
        return render_template("db_view.html", table=postgres.get_table("batch"),
                               column_names=postgres.get_table_columns("batch"))
