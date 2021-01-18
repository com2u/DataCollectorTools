import json

from flask import render_template, request, redirect
from flask_classful import FlaskView, route


class ConfigView(FlaskView):
    def index(self):
        route_base = "/config/"
        with open("parameters.json") as file:
            data = json.load(file)
            standard_parameter = [data["standart_postgres_url"],
                                  data["standart_postgres_user"], data["standart_postgres_db"],
                                  data["standart_limit_table_length"]
                                  ]
            user_parameter = [data["postgres_url"], data["postgres_user"], data["postgres_db"],
                              data["limit_table_length"]]
        return render_template("config_view.html", standard_parameter=standard_parameter, user_parameter=user_parameter)

    @route('/saveconfigvalues/', methods=['POST'])
    def save_config_values(self):
        file = open("parameters.json", "r")
        data = json.load(file)
        for parameter in ['postgres_url', 'postgres_user', 'postgres_pw', 'postgres_db', 'limit_table_length']:
            if request.form.get(parameter) != "":
                data[parameter] = request.form.get(parameter)
        file = open("parameters.json", "w")
        json.dump(data, file)
        return redirect("/config")
