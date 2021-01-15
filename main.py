from flask_app_wrapper import *
if __name__ == '__main__':
    webserver = FlaskAppWrapper('webserver')
    webserver.run()
