from app import service
from flask import Blueprint, request, jsonify

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json

    # Validation
    if not data or "name" not in data or "email" not in data or "password" not in data:
        return jsonify({"error": "missing required fields"}), 400


    if not isinstance(data["name"], str):
        return jsonify({"error": "Name must be a string"}), 400

    if not isinstance(data["email"], str):
        return jsonify({"error": "Email must be a string"}), 400

    if not isinstance(data["password"], str):
        return jsonify({"error": "Password must be a non-empty string"}), 400

    result, status = service.signup(data)
    return jsonify(result), status

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    if not data or "email" not in data or "password" not in data:
        return jsonify({"error": "missing email or password."}), 400

    result, status = service.login(data)
    return jsonify(result), status