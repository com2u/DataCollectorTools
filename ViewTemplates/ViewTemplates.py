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
    defaultrowcount integer,
    rowcountoptions integer[],
    invisiblecolumns text[] COLLATE pg_catalog."default",
    PRIMARY KEY (id))
    """)


@view_templates.route("/", methods=["GET", "POST"])
def get_all_templates():
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
        if 'rowcountoptions' not in params or len(params['rowcountoptions']) == 0:
            params[param] = "{}"
        elif param in params:
            params['rowcountoptions'] = str({int(option) for option in params['rowcountoptions'] if option != ''})
        if 'invisiblecolumns' not in params or len(params['invisiblecolumns']) == 0:
            params[param] = "{}"
        elif param in params:
            params['invisiblecolumns'] = {str(column) for column in params['invisiblecolumns'] if column  != ''}
            if len(params['invisiblecolumns']) == 0:
                params['invisiblecolumns'] = "{}"
            else:
                 params['invisiblecolumns'] =  str(params['invisiblecolumns'])

        
        database = get_postgres_instance(dbname="dbtools")
        id = database.engine.execute(
            f"""INSERT INTO viewfilter (viewname, defaultrowcount, rowcountoptions, invisiblecolumns) VALUES('{params['viewname']}', {int(params['defaultrowcount'])}, '{params['rowcountoptions']}', '{params['invisiblecolumns']}') RETURNING id;""").fetchone()[0]
        return jsonify(id=id)


@view_templates.route("/delete/<id>", methods=["DELETE"])
def delete_view_template(id):
    database = get_postgres_instance(dbname="dbtools")
    return jsonify(success=database.delet_view_template(id))
