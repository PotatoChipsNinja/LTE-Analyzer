from flask import Blueprint, request

admin = Blueprint("admin", __name__)


@admin.route("/api/admin/login", methods=["POST"])
def login():
    return {"success": True}


@admin.route("/api/admin/passwd", methods=["POST"])
def passwd():
    return {"success": True}


@admin.route("/api/admin/userlist", methods=["GET"])
def get_user_list():
    return []


@admin.route("/api/admin/createUser", methods=["POST"])
def create_user():
    return {"success": True}


@admin.route("/api/admin/removeUser", methods=["POST"])
def remove_user():
    return {"success": True}


@admin.route("/api/admin/DBInfo", methods=["GET"])
def get_db_info():
    return {
        "host": "127.0.0.1",
        "port": 3306,
        "db": "ltdb",
        "username": "root",
        "password": "123456",
        "interactiveTimeout": 0,
        "waitTimeout": 0,
        "partition": "",
        "queryCacheSize": ""
    }


@admin.route("/api/admin/setTimeout", methods=["POST"])
def set_timeout():
    return {"success": True}


@admin.route("/api/admin/setCache", methods=["POST"])
def set_query_cache_size():
    return {"success": True}