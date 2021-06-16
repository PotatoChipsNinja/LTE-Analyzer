from flask import Blueprint, request

advanced = Blueprint("advanced", __name__)


@advanced.route("/api/advanced/c2i", methods=["GET"])
def c2i():
    return getc2i()


@advanced.route("/api/advanced/c2i3", methods=["GET"])
def c2i3():
    x = request.args.get("x")
    return getc23i(x)
