from flask import Blueprint
import simplejson as json


bp = Blueprint("user", import_name=__name__, url_prefix="/user")


@bp.route("/health")
def health():
    return json.dumps({"health": "alive"})


@bp.route("/all", methods=["GET"])
def show_users():
    return json.dumps({"index": "hello"})


@bp.route("/<int:_id>", methods=["GET"])
def show_user(_id):
    return json.dumps({"index": _id})


@bp.route("/new", methods=["POST"])
def create_user():
    return json.dumps({"index": "hello"})


@bp.route("/<int:_id>", methods=["PATCH"])
def update_user(_id):
    return json.dumps({"index": _id})


@bp.route("/new", methods=["DELETE"])
def delete_user():
    return json.dumps({"index": "hello"})
