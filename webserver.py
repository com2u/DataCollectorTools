from flask import Flask

from Modules.config_view import *
from Modules.db_postgres_view import *
from Modules.db_sqlite_view import *


class FlaskAppWrapper(object):
    app = None

    def __init__(self, name):
        self.app = Flask(name)
        self.register_views()

    def run(self):
        self.app.run()

    def register_views(self):
        PostgresView.register(self.app)
        ConfigView.register(self.app)
        SqliteView.register(self.app)
