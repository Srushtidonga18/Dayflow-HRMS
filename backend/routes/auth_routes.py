from flask import Blueprint, request, jsonify
import jwt
from config import Config
from utils.password_hash import hash_password, verify_password
from database.db_connection import get_db_connection
from models.user import UserMode
from werkzeug.security import check_password_hashl
from models import User

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

from flask import Blueprint

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/test", methods=["GET"])
def auth_test():
    return {"message": "Auth API working"}


@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json

    password_hash = hash_password(data["password"])

    user_id = UserModel.create_user(
        employee_id=data["employee_id"],
        company_code=data["company_code"],
        first_name=data["first_name"],
        last_name=data["last_name"],
        email=data["email"],
        phone=data.get("phone"),
        password_hash=password_hash,
        role=data["role"],
        year_of_joining=data["year_of_joining"]
    )

    return jsonify({
        "message": "User registered successfully",
        "user_id": user_id
    }), 201


# ✅ LOGIN
from flask import jsonify, request
from models import User
from werkzeug.security import check_password_hash
import jwt

@auth_bp.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json()

    user = User.query.filter_by(email=data["email"]).first()

    if not user or not check_password_hash(user.password, data["password"]):
        return jsonify({"message": "Invalid credentials"}), 401

    token = jwt.encode(
        {"user_id": user.id},
        "SECRET_KEY",
        algorithm="HS256"
    )

    return jsonify({
        "token": token,
        "role": user.role,
        "user": {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "employee_id": user.employee_id,
            "company_code": user.company_code,
            "phone": user.phone,
            "year_of_joining": user.year_of_joining
        }
    }), 200
