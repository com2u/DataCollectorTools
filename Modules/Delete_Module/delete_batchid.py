from flask_classful import FlaskView


class TestView(FlaskView):
    def index(self):
        return "test"