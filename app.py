from flask import Flask
from flask.globals import current_app
from flask_oidc import OpenIDConnect


def init_app():
    """Create Flask application."""
    app = Flask(__name__, static_folder='static', static_url_path='')
    app.config.from_object('config.Config')

    with app.app_context():
        from Startscreen.StartView import start
        from auth.LogoutView import auth
        from Home.DashboardView import dash
        from LoggingHandler.LogView import log
        
        # Register Blueprints
        app.register_blueprint(start)
        app.register_blueprint(auth)
        app.register_blueprint(dash)
        app.register_blueprint(log)

        return app

def init_oidc():
    oidc = OpenIDConnect(current_app)
    return oidc

def init_logger():
    from LoggingHandler.LogHandler import SVLog
    NickModul = SVLog()

    logger = NickModul.getLogger('Flask_DBTool')
    logger.setLevel(10)

    ch = NickModul.StreamHandler()
    ch.setLevel(10)

    formatter = NickModul.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


if __name__ == "__main__":
    app = init_app()
    app.run(port=5000)
