from flask import Flask
from flask.globals import current_app
from flask_oidc import OpenIDConnect
import json

def init_app():
    """Create Flask application."""
    app = Flask(__name__, static_folder='static', static_url_path='')
    app.config.from_object('config.Config')

    with app.app_context():
        from Startscreen.StartView import start
        from auth.LogoutView import auth
        from Home.DashboardView import dash
        from Table.Table import table_interface
        from ExportBackend.Export import process_interface
        from ExportFrontend.export_frontend import export
        from Config.db_config import config_interface
        from Delete.Delete import delete_interface
       
        
        # Register Blueprints
        app.register_blueprint(start)
        app.register_blueprint(auth)
        app.register_blueprint(dash)
        app.register_blueprint(table_interface)
        app.register_blueprint(process_interface)
        app.register_blueprint(export)
        app.register_blueprint(config_interface)
        app.register_blueprint(delete_interface)

        return app

def init_oidc():
    oidc = OpenIDConnect(current_app)
    return oidc


if __name__ == "__main__":
    app = init_app()
    with open("parameters.json") as file:
        data = json.load(file)
    flask_port = data["flask_port"]
    app.run(host="0.0.0.0", port=flask_port)
