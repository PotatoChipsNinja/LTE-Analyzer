from flask import Blueprint, request
from src.db import db36
from src.db import db37


advanced = Blueprint("advanced", __name__)


@advanced.route("/api/advanced/c2i", methods=["GET"])
def c2i():
    ret = db36.select_all_from_tbC2inew()
    print(ret)
    return {
        "result": db36.select_all_from_tbC2inew()
    }


@advanced.route("/api/advanced/c2i3", methods=["GET"])
def c2i3():
    x = request.args.get("x")
    return getc23i(x)
