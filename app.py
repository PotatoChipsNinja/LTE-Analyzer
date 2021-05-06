import os
import math
import pandas as pd

from flask import Flask, render_template, request
from flask_sockets import Sockets
from src.api.admin import admin
from src.api.user import user
from src.api.data import data
from src.api.query import query
from src.db.tb import *
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

app = Flask(__name__,
            template_folder="public",
            static_folder="public",
            static_url_path="/")
app.register_blueprint(admin)
app.register_blueprint(user)
app.register_blueprint(data)
app.register_blueprint(query)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<path>")
def error(path):
    return render_template("index.html")

sockets = Sockets(app)
@sockets.route("/api/data/import")
def import_file(ws):
    file = ws.receive()
    name = str(request.args.get("table")) + "." + request.args.get("type")
    if not os.path.exists("upload/"):
        os.mkdir("upload/")
    file_path = "upload/" + name
    with open(file_path, "wb") as fp:
        fp.write(file)
    if request.args.get("type") == "csv":
        df = pd.read_csv(file_path)
    elif request.args.get("type") == "xlsx":
        df = pd.read_excel(file_path)
    block_size = 50
    data_len = df.shape[0]
    for i in range(math.ceil(data_len / block_size)):
        block = df.iloc[i * block_size:min((i + 1) * block_size, data_len)]
        data_bulkinsert(int(request.args.get("table")), block)
        print("send {} to web server".format(min((i + 1) * block_size, data_len) * 100 // data_len))
        ws.send(str(min((i + 1) * block_size, data_len) * 100 // data_len))
    ws.send("finish")


if __name__ == "__main__":
    server = WSGIServer(
        ('127.0.0.1', 3000),
        app,
        handler_class=WebSocketHandler,
    )
    print("server start ...")
    server.serve_forever()
