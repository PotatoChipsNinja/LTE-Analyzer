from flask import Blueprint, request
import json

admin = Blueprint("admin", __name__)


@admin.route("/api/admin/login", methods=["POST"])
def login():
    return {"success": True}