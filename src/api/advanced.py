from flask import Blueprint, request
from src.db.query import select_all_from_tbC2inew, select_all_from_tbC2i3
from lib.draw import draw

advanced = Blueprint("advanced", __name__)


@advanced.route("/api/advanced/c2i", methods=["GET"])
def c2i():
    tmp = select_all_from_tbC2inew()
    ret = []
    for _, row in tmp.iterrows():
        ret.append({
            "servingSector": row["ServingSector"],
            "interfereringSector": row["InterferingSector"],
            "mean": row["mean"],
            "std": row["std"],
            "diff9": row["PrbC2I9"],
            "abs6": row["PrbABS6"]
        })
    return {"result": ret}


@advanced.route("/api/advanced/c2i3", methods=["GET"])
def c2i3():
    x = request.args.get("x")
    tmp = select_all_from_tbC2i3(x)
    ret = []
    for _, row in tmp.iterrows():
        ret.append([row["SectorA"], row["SectorB"], row["SectorC"]])
    return {"result": ret}


@advanced.route("/api/advanced/louvain", methods=["GET"])
def louvain():
    x = float(request.args.get("x"))
    return {"img": draw.get_base64(x)}
