from flask import Blueprint, request, g

bp = Blueprint("heaps", __name__, url_prefix="/heaps")

@bp.route("/", methods=["GET"])
def list_heaps():
    return g.heaps

@bp.route("/<name>/push", methods=["POST"])
def push_heap(name):
    value = request.arg.get("value", type=int)
    return {"success": True}


@bp.before_app_first_request
def setup():
    g.heaps = {}