from flask import jsonify, request
from app import app
from app import service

# Welcome page:
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Inventory API running"})


# Add new inventory item:
@app.route("/inventory", methods=["POST"])
def create_item():
    data = request.json

    if not data or "name" not in data or "quantity" not in data:
        return jsonify({"error": "Missing required fields"}), 400

    if not isinstance(data["name"], str):
        return jsonify({"error": "Name must be string"}), 400

    if not isinstance(data["quantity"], int):
        return jsonify({"error": "Quantity must be integer"}), 400

    result, status = service.create_item(data)
    return jsonify(result), status


# Get specific item:
@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_item(item_id):
    result, status = service.get_item(item_id)
    return jsonify(result), status


# Get all items:
@app.route("/inventory", methods=["GET"])
def get_inventory():
    result, status = service.get_inventory()
    return jsonify(result), status


# Update item quantity:
@app.route("/inventory/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.json

    if not data:
        return jsonify({"error": "No data provided"}), 400

    if "name" in data and not isinstance(data["name"], str):
        return jsonify({"error": "Name must be string."}), 400

    if "quantity" in data and not isinstance(data["quantity"], int):
        return jsonify({"error": "Quantity must be integer"}), 400
    result, status = service.update_item(item_id, data)
    return jsonify(result), status


# DELETE - Remove item (only if quantity is 0)
@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    result, status = service.delete_item(item_id)

    if status == 204:
        return "", 204

    return jsonify(result), status