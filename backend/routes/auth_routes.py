from flask import Blueprint, request, jsonify
import jwt
from config import Config
from utils.password_hash import hash_password, verify_password
from database.db_connection import get_db_connection
from models.user import UserModel

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
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = UserModel.get_user_by_email(data["email"])

    if not user:
        return {"message": "Invalid email"}, 401

    if not verify_password(data["password"], user[7]):  # password_hash index
        return {"message": "Invalid password"}, 401

    return {
        "message": "Login successful",
        "user_id": user[0],
        "role": user[8]
    }