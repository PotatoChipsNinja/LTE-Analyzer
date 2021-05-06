from flask import Blueprint, request, send_from_directory
from src.db.tb import *

data = Blueprint("data", __name__)


@data.route("/api/data/export", methods=["GET"])
def export():
    file_name = data_export(int(request.args.get("table")), request.args.get("type"))
    return {
        "url": send_from_directory("download/", file_name, as_attachment=True),
    }
