from app import storage
from mysql.connector import errors
import bcrypt
import jwt
import os

# Create new item:

def create_item(data):
    allowed_fields = ["name", "quantity"]

    for key in data.keys():
        if key not in allowed_fields:
            return {"error": f"Invalid field: {key}"}, 400

    if data["name"].strip() == "":
        return {"error": "Name cannot be empty"}, 400

    if data["quantity"] < 0:
        return {"error": "Quantity cannot be negative"}, 400

    try:
        item = storage.create_item(data["name"], data["quantity"])
        return item, 201

    except errors.IntegrityError:
        return {"error": "Item with this name already exists"}, 409


# Get specific item:
def get_item(item_id):
    item = storage.get_item(item_id)

    if not item:
        return {"error": "Item not found"}, 404

    return item, 200

# Get all items:
def get_inventory():
    items = storage.get_inventory()
    return items, 200


# Update item:
def update_item(item_id, data):
    item = storage.get_item(item_id)

    if not item:
        return {"error": "Item not found"}, 404

    allowed_fields = ["name", "quantity"]

    for key in data.keys():
        if key not in allowed_fields:
            return {"error": f"Invalid field: {key}"}, 400

    if "name" in data:
        if data["name"].strip() == "":
            return {"error": "Invalid name"}, 400

    if "quantity" in data:
        if data["quantity"] < 0:
            return {"error": "Invalid quantity"}, 400

    updated = storage.update_item(item_id, data)
    return updated, 200


# Delete item:
def delete_item(item_id):
    item = storage.get_item(item_id)

    if not item:
        return {"error": "Item not found."}, 404

    if item["quantity"] > 0:
        return {
            "error": "Cannot delete item with remaining quantity",
            "current_quantity": item["quantity"]
        }, 409

    storage.delete_item(item_id)
    return {}, 204


# create new user:
def signup(data):
    name = data["name"]
    email = data["email"]
    password = data["password"]

    # Validation:
    if not name.strip():
        return {"error": "name can't be empty"}, 400

    if not email.strip():
        return {"error": "email can't be empty"}, 400

    if not password.strip():
        return {"error": "password can't be empty"}, 400

# Password hashing
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    result = storage.signup(name, email, hashed_password)
    return result

# User login:
def login(data):
    email = data["email"]
    password = data["password"]

    user = storage.login(email)

    if not user:
        return {"error": "invalid mail or password"}, 401

    stored_hash = user["password_hash"]
    if isinstance(stored_hash, str):
        stored_hash = stored_hash.encode("utf-8")

    if not bcrypt.checkpw(password.encode("utf-8"), stored_hash):
        return {"error": "invalid mail or password"}, 401

    # Generate token:
    user_info = {
        "user_id": user["id"],
        "user_email": user["email"]
    }

    SECRET_KEY = os.getenv("SECRET_KEY")
    token = jwt.encode(user_info, SECRET_KEY, algorithm="HS256")

    if isinstance(token, bytes):
        token = token.decode("utf-8")

    return {"token": token}, 200