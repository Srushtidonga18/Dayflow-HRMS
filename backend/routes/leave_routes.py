from flask import Blueprint, request, jsonify
from utils.auth_middleware import token_required
from database.db_connection import get_db_connection
from models.leave import LeaveModel

leave_bp = Blueprint("leave", __name__, url_prefix="/leave")

from flask import Blueprint

leave_bp = Blueprint("leave_bp", __name__)

@leave_bp.route("/", methods=["GET"])
def leave_home():
    return {"message": "Leave GET API working"}


@leave_bp.route("/apply", methods=["POST"])
def apply_leave():
    data = request.json

    LeaveModel.apply_leave(
        user_id=data["user_id"],
        leave_type_id=data["leave_type_id"],
        start_date=data["start_date"],
        end_date=data["end_date"],
        reason=data.get("reason")
    )

    return jsonify({"message": "Leave applied successfully"}), 201
