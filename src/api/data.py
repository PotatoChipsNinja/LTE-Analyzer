import os

from flask import Blueprint, request, send_from_directory
from src.db.tb import *

data = Blueprint("data", __name__)


@data.route("/api/data/export", methods=["GET"])
def export():
    print(int(request.args.get("table")), request.args.get("type"),
          type(request.args.get("type")))
    file_name = data_export(int(request.args.get("table")),
                            request.args.get("type"))
    return {
        "url": "http://127.0.0.1:3000/download/" + file_name,
    }


@data.route("/download/<filename>")
def download(filename):
    return send_from_directory("download", filename, as_attachment=True)
