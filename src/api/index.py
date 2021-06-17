from flask import Blueprint, request
from src.db.tb import add_index, del_index, select_index

index = Blueprint("index", __name__)


@index.route("/api/index/getIndex", methods=["GET"])
def getIndex():
    ret = []
    for i in range(1, 4):
        tmp = select_index(i)
        for ls in tmp:
            try:
                ret.append({"table": ls[0], "name": ls[1], "key": ls[2]})
            except IndexError:
                continue
    return {"indexes": ret}


@index.route("/api/index/addIndex", methods=["POST"])
def addIndex():
    table = request.form["table"]
    name = request.form["name"]
    key = request.form["key"]
    print(key, type(key))
    if table == "tbcell":
        table = 1
    elif table == "tbprb":
        table = 3
    else:
        table = 2
    return {"success": add_index(table, key, name)}


@index.route("/api/index/removeIndex", methods=["POST"])
def delIndex():
    table = request.form["table"]
    if table == "tbcell":
        table = 1
    elif table == "tbprb":
        table = 3
    else:
        table = 2
    return {"success": del_index(table, request.form["name"])}
