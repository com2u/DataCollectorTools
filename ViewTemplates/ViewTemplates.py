from flask import Blueprint

view_templates = Blueprint(
    'view_templates', __name__, url_prefix="/view_templates"
)

@view_templates.route("/", methods=["GET"])
def get_all_templates():
    pass

@view_templates.route("/id/<view_id>", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def get_by_view_id():
    pass

@view_templates.route("/name/<view_name>", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def get_by_view_name():
    pass



