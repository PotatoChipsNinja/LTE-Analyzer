from flask import Blueprint, request

user = Blueprint("user", __name__)


@user.route("/api/user/login", methods=["POST"])
def login():
    return {"Success": True}


@user.route("/api/user/passwd", methods=["POST"])
def passwd():
    return {"Success": True}