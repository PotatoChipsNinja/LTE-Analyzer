from flask import Blueprint, request
from src.db.query import *

query = Blueprint("query", __name__)


@query.route("/api/query/sector", methods=["GET"])
def sector():
    if request.args.get("sectorID") is not None:
        ret = {}
        d = select_SectorAllo_From_tbCell_SectorId(request.args.get("sectorID"))
        for key, value in d.items():
            ret[key] = value[0]
        return {"result": ret}
    elif request.args.get("sectorName") is not None:
        ret = {}
        d = select_SectorAllo_From_tbCell_SectorName(
            request.args.get("sectorName"))
        for key, value in d.items():
            ret[key] = value[0]
        return {"result": ret}


@query.route("/api/query/eNodeB", methods=["GET"])
def eNodeB():
    if request.args.get("eNodeBID") is not None:
        ret = {}
        d = select_SectorAllo_From_tbCell_eNodeBId(request.args.get("eNodeBID"))
        for key, value in d.items():
            ret[key] = value[0]
        return {"result": ret}
    elif request.args.get("eNodeBName") is not None:
        ret = {}
        d = select_SectorAllo_From_tbCell_eNodeBName(
            request.args.get("eNodeBName"))
        for key, value in d.items():
            ret[key] = value[0]
        return {"result": ret}


@query.route("/api/query/kpi", methods=["GET"])
def kpi():
    ls = select_Data_From_tbKPI_SectorName(request.args.get("name"),
                                           request.args.get("attribute"),
                                           request.args.get("start"),
                                           request.args.get("end"))
    ret = [float(x[0]) for x in ls]
    return {"value": ret}


@query.route("/api/query/prb", methods=["GET"])
def prb():
    ls = select_Data_From_tbPRB_SectorName(request.args.get("name"),
                                           request.args.get("prb"),
                                           request.args.get("start"),
                                           request.args.get("end"))
    ret = [float(x[0]) for x in ls]
    return {"value": ret}


@query.route("/api/query/candidate", methods=["GET"])
def candidate():
    type = request.args.get("key")
    ls = select_BasicData_From_tb(int(type))
    ret = [x[0] for x in ls]
    return {"candidate": ret}
