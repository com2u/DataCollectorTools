from flask import Blueprint, jsonify, request
from db_actions import get_postgres_instance

view_templates = Blueprint(
    'view_templates', __name__, url_prefix="/view_templates"
)


@view_templates.before_app_first_request
def database_initialization():
    database = get_postgres_instance(dbname="dbtools")
    database.engine.execute("""
    CREATE TABLE IF NOT EXISTS public.viewfilter
    (
    id SERIAL,
    viewname text COLLATE pg_catalog."default",
    setting text,
    PRIMARY KEY (id))
    """)


@view_templates.route("/", methods=["GET", "POST", "DELETE"])
def view_template():
    if request.method == 'GET':
        database = get_postgres_instance(dbname="dbtools")
        table_names = database.get_table_names()
        if "viewfilter" in table_names:
            return jsonify({"data": [dict(row) for row in database.get_table("viewfilter")]})
    if request.method == 'POST':
        params = request.values.to_dict(flat=False)
        #formating params to fit database connection string
        if 'viewname' not in params:
            params['viewname'] = ''
        elif 'viewname' in params:
            params['viewname'] = params['viewname'][0]
        params['options'] = params['options'][0]
        database = get_postgres_instance(dbname="dbtools")
        querystring = f"""
        INSERT INTO viewfilter (viewname, setting)
        VALUES('{params['viewname']}', '{params["options"]}')
        RETURNING id;"""
        id = database.engine.execute(querystring).fetchone()[0]
        return jsonify(id=id)
    if request.method == "DELETE":
        params = request.values.to_dict(flat=False)
        id = params["id"][0]
        database = get_postgres_instance(dbname="dbtools")
        return jsonify(success=database.delet_view_template(id))