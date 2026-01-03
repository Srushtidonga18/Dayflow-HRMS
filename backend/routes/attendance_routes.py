from flask import Blueprint, jsonify, request
from utils.auth_middleware import token_required
from database.db_connection import get_db_connection
from datetime import date, datetime
from models.attendance import AttendanceModel

attendance_bp = Blueprint("attendance", __name__, url_prefix="/attendance")

from flask import Blueprint

attendance_bp = Blueprint("attendance_bp", __name__)

@attendance_bp.route("/", methods=["GET"])
def attendance_home():
    return {"message": "Attendance GET API working"}



@attendance_bp.route("/", methods=["POST"])
def mark_attendance():
    data = request.json

    AttendanceModel.mark_attendance(
        user_id=data["user_id"],
        date=data["date"],
        check_in=data["check_in"],
        check_out=data.get("check_out"),
        status=data["status"],
        work_hours=data.get("work_hours")
    )

    return jsonify({"message": "Attendance marked successfully"}), 201
