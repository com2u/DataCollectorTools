from flask import Blueprint, jsonify, request, send_file, after_this_request
import db_actions
from pathlib import Path

delete_interface = Blueprint(
    'delete_interface', __name__, url_prefix="/delete_interface")


@delete_interface.route('/db')
def delete_db():
    database = db_actions.get_postgres_instance()
    return jsonify(database.delete(filter=request.values.to_dict()))


@delete_interface.route("/pictures")
def delete_pictures():
    database = db_actions.get_postgres_instance()
    pathes_to_pictures = database.get_table_column_values(
        "trigger_image_links", "image1", filter=request.values.to_dict())
    missing_files = []
    deleted_files = []
    if len(pathes_to_pictures) > 0:
        for picture in pathes_to_pictures:
            picture = Path(picture)
            if picture.exists():
                picture.unlink()
                deleted_files.append(picture)
            else:
                missing_files.append(picture)

        return jsonify(success=True, deleted_files=len(deleted_files), missing_files=len(missing_files))
    return jsonify(success=False)
