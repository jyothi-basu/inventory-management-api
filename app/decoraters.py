from functools import wraps
from flask import request, jsonify
import jwt
import os

def get_required_env(name):
    value = os.getenv(name)

    if not value:
        raise RuntimeError(f"{name} environment variable is required")

    return value

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

        SECRET_KEY = get_required_env("SECRET_KEY")

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        except Exception:
            return jsonify({"error": "Invalid token"}), 401

        return f(*args, **kwargs)

    return decorator
