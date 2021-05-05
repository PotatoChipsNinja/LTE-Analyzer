from flask import Blueprint, request
from src.db.query import *

query = Blueprint("query", __name__)

@query.route("/api/query/sector", methods=["GET"])
def sector():
    print(request.args.get("sectorID"), request.args.get("sectorName"))

@query.route("/api/query/candidate", methods=["GET"])
def candidate():
    type = request.args.get("key")
    ls = select_BasicData_From_tb(int(type))
    ret = [x[0] for x in ls]
    return {"candidate": ret}