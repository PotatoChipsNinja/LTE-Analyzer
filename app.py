from flask import Flask, render_template, request
from flask_sockets import Sockets
from flask_socketio import SocketIO
from werkzeug.exceptions import BadRequest
from src.api.admin import admin
from src.api.user import user
from src.api.data import data
from src.api.query import query

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


# @app.errorhandler(BadRequest)
# def handle_bad_request(e):
#     return render_template("index.html")


# app.register_error_handler(404, handle_bad_request)
@app.route("/<path>")
def error(path):
    return render_template("index.html")


# sockets = Sockets(app)
# @sockets.route("/api/data/import")
# def import_file(ws):
#     print("yes")
#     if request.method == "GET":
#         print("yes")

# socketio = SocketIO(app)

# @socketio.on("import_request", namespace="/import")
# def import_data(data):
#     print(data["type"], data["table"], type(data["file"]))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="3000", debug=True)
