from flask import Flask

from Modules.config_view import *
from Modules.db_postgres_view import *
from Modules.db_sqlite_view import *
from Modules.two_tables_view import TwotablesView


class FlaskAppWrapper(object):
    app = None

    def __init__(self, name):
        self.app = Flask(name)
        self.register_views()

    def run(self):
        self.app.run(debug=True)

    def register_views(self):
        PostgresView.register(self.app)
        ConfigView.register(self.app)
        SqliteView.register(self.app)
        TwotablesView.register(self.app)
