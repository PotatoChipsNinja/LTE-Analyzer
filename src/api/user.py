from flask import Blueprint, request
from src.db.user import user_signin, user_change_passwd

user = Blueprint("user", __name__)


@user.route("/api/user/login", methods=["POST"])
def login():
    return {
        "success":
            True if user_signin(request.form["username"],
                                request.form["passwd"], 2) else False
    }


@user.route("/api/user/passwd", methods=["POST"])
def passwd():
    return {
        "success":
            True if user_change_passwd(request.form["username"],
                                       request.form["oldPasswd"],
                                       request.form["newPasswd"], 2) else False
    }
