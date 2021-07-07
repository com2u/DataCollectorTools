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
    defaultrowcount integer NOT NULL,
    invisiblecolumns text[] COLLATE pg_catalog."default",
    tablename text,
    PRIMARY KEY (id))
    """)


@view_templates.route("/", methods=["GET", "POST"])
def all_view_templates():
    if request.method == 'GET':
        database = get_postgres_instance(dbname="dbtools")
        table_names = database.get_table_names()
        if "viewfilter" in table_names:
            return jsonify({"data": [dict(row) for row in database.get_table("viewfilter")]})
    if request.method == 'POST':
        params = request.values.to_dict(flat=False)
        #formating params to fit database connection string
        for param in ['viewname', 'defaultrowcount']:
            if param not in params:
                params[param] = ''
            elif param in params:
                params[param] = params[param][0]
        if "invisiblecolumns" not in params or len(params["invisiblecolumns"]) == 0:
            params[param] = "{}"
        elif "invisiblecolumns" in params:
            params["invisiblecolumns"] = {str(column) for column in params["invisiblecolumns"] if column  != ""}
            if len(params["invisiblecolumns"]) == 0:
                params["invisiblecolumns"] = "{}"
            else:
                 params["invisiblecolumns"] =  params["invisiblecolumns"]

        database = get_postgres_instance(dbname="dbtools")
        querystring = f"""
        INSERT INTO viewfilter (viewname, defaultrowcount, invisiblecolumns)
        VALUES('{params['viewname']}', {int(params['defaultrowcount'])}, '{str(params["invisiblecolumns"]).replace("'", '"')}')
        RETURNING id;"""
        id = database.engine.execute(querystring).fetchone()[0]
        return jsonify(id=id)

@view_templates.route("/<id>", methods=["GET", "DELETE"])
def view_template(id):
    if request.method == "DELETE":
        database = get_postgres_instance(dbname="dbtools")
        return jsonify(success=database.delet_view_template(id))
    if request.method == "GET":
        pass