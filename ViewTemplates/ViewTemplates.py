from flask import Blueprint, jsonify, request
from db_actions import get_postgres_instance

view_templates = Blueprint(
    'view_templates', __name__, url_prefix="/view_templates"
)

@view_templates.route("/", methods=["GET", "POST"])
def get_all_templates():
    if request.method == 'GET':
        database = get_postgres_instance(dbname="dbtools")
        table_names = database.get_table_names()
        if "viewfilter" in table_names:
            return jsonify({"data": [dict(row) for row in database.get_table("viewfilter")]})
    if request.method == 'POST':
        return ""

@view_templates.route("/delete/<id>", methods=["DELETE"])
def delete_view_template(id):
    database = get_postgres_instance(dbname="dbtools")
    return jsonify(success=database.delet_view_template(id))
