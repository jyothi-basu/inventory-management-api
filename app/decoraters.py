from functools import wraps
from flask import request, jsonify
import jwt
import os

# Defining route protection:
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None

        auth_header = request.headers.get("Authorization")

        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]

        if not token:
            return jsonify({"error": "token missing"}), 401

        try:
            SECRET_KEY = os.getenv("SECRET_KEY")
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        except Exception:
            return jsonify({"error": "Invalid token"}), 401

        return f(*args, **kwargs)

    return decorator