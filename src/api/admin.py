from flask import Blueprint, request
from src.db.user import *
from src.db.common import *
import time

admin = Blueprint("admin", __name__)


@admin.route("/api/admin/login", methods=["POST"])
def login():
    return {
        "success":
            True if user_signin(request.form["username"],
                                request.form["password"], 1) else False
    }


@admin.route("/api/admin/passwd", methods=["POST"])
def passwd():
    return {
        "success":
            True if user_change_passwd(request.form["username"],
                                       request.form["oldPasswd"],
                                       request.form["newPasswd"], 1) else False
    }


@admin.route("/api/admin/userList", methods=["GET"])
def get_user_list():
    ls = user_get_list(2)
    ret = []
    for info in ls:
        ret.append({"username": info[0], "time": str(info[1])[:10]})
    return {"users": ret}


@admin.route("/api/admin/createUser", methods=["POST"])
def create_user():
    return {
        "success":
            True if user_add(request.form["username"], request.form["passwd"],
                             1) else False
    }


@admin.route("/api/admin/removeUser", methods=["POST"])
def remove_user():
    return {"success": True if user_delete(request.form["username"], 2) else False}


@admin.route("/api/admin/DBInfo", methods=["GET"])
def get_db_info():
    return db_get_inf()
    # return {
    #     "host": "127.0.0.1",
    #     "port": 3306,
    #     "db": "ltdb",
    #     "username": "root",
    #     "password": "123456",
    #     "interactiveTimeout": 0,
    #     "waitTimeout": 0,
    #     "partition": "",
    #     "queryCacheSize": ""
    # }


@admin.route("/api/admin/setTimeout", methods=["POST"])
def set_timeout():
    db_change_timeout(request.form["interactiveTimeout"],
                      request.form["waitTimeout"])
    return {"success": True}


@admin.route("/api/admin/setCache", methods=["POST"])
def set_query_cache_size():
    db_change_cache_size(request.form["queryCacheSize"])
    return {"success": True}