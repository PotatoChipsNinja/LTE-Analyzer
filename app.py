import os

from flask import Flask, render_template, request
from flask_sockets import Sockets
from src.api.admin import admin
from src.api.user import user
from src.api.data import data
from src.api.query import query
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
    with open("upload/" + name, "wb") as fp:
        fp.write(file)


if __name__ == "__main__":
    server = WSGIServer(
        ('127.0.0.1', 3000),
        app,
        handler_class=WebSocketHandler,
    )
    print("server start ...")
    server.serve_forever()
