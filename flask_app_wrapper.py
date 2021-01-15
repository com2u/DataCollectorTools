from flask import Flask

from Modules.Delete_Module.delete_batchid import TestView


class FlaskAppWrapper(object):
    app = None

    def __init__(self, name):
        self.app = Flask(name)
        self.register_views()

    def run(self):
        self.app.run()

    def register_views(self):
        TestView.register(self.app)
