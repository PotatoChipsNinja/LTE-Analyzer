from flask import Blueprint, request
from flask_socketio import socketio
from werkzeug.utils import secure_filename
import os
import pandas as pd
import math

UPLOAD_FOLDER = "./data/"
ALLOWED_EXTENSIONS = {"xlsx", "csv"}

data = Blueprint("data", __name__)

tables = {1: "tbCell", 2: "tbKPI", 3: "tbPRB", 4: "tbMROData"}

uid = 0
process = {}

# @data.route("/api/data/import", methods=["POST"])
# def import_file():
#     global uid
#     print(request.files, request.form)
#     file = request.files["file"]
#     file_name = secure_filename(file.filename)
#     if not os.path.exists(UPLOAD_FOLDER):
#         os.makedirs(UPLOAD_FOLDER)
#     file_path = os.path.join(UPLOAD_FOLDER, file_name)
#     file.save(file_path)
#     block_size = 50
#     cur_uid = uid
#     uid += 1
#     process[cur_uid] = {"uuid": cur_uid, "progress": 0, "file_path": file_path}

#     return {"uuid": cur_uid}

# @data.route("/api/data/progress", methods=["GET"])
# def progress():
#     # if request.form["type"] == "csv":
#     #     df = pd.read_csv(file_path)
#     # else:
#     #     df = pd.read_excel(file_path)
#     # data_len = df.shape[0]
#     data_len = 1000

#     for i in range(math.ceil(data_len / block_size)):
#         block = df.iloc[i * block_size:min((i + 1) * block_size, df.shape[0])]
#         process[cur_uid] = int(i * block * 100 / data_len)
#         #data_bulkinsert(tables[request.form["table"]], block)  # 接口undefined
#         yield {
#             "finished": True if process[cur_uid][progress] == 100 else False,
#             "progress": process[cur_uid][progress]
#         }

# @data.route("/api/data/export", methods=["GET"])
