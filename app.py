# Inventory Management API - Complete CRUD with validation

from flask import Flask, jsonify, request

app = Flask(__name__)

# Inventory data storage
inventory = {}
next_id = 1

# home- welcome page.
@app.route("/", methods=["GET"])
def home():
    return """
    <html><head><title> Home - inventory management API</title></head>
    
    <h1> Welcome to inventory management project</h1></html>"""


# CREATE - Add new inventory item
@app.route("/inventory", methods=["POST"])
def create_item():
    global next_id
    data = request.json

    # Check for missing fields
    if not data or "name" not in data or "quantity" not in data:
        return jsonify({"error": "Missing required fields"}), 400

    # Validate name
    if not isinstance(data["name"], str):
        return jsonify({"error": "Name must be string"}), 400
    
    if data["name"].strip() == "":
        return jsonify({"error": "Name cannot be empty"}), 400

    # Validate quantity
    if not isinstance(data["quantity"], int):
        return jsonify({"error": "Quantity must be integer"}), 400
    
    if data["quantity"] < 0:
        return jsonify({"error": "Quantity cannot be negative"}), 400

    # Create item
    inventory_data = {
        "id": next_id,
        "name": data["name"].strip(),
        "quantity": data["quantity"]
    }

    inventory[next_id] = inventory_data
    next_id += 1

    return jsonify(inventory_data), 201


# READ - Get specific item
@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_item(item_id):
    if item_id in inventory:
        return jsonify(inventory[item_id]), 200
    else:
        return jsonify({"error": "Item not found"}), 404


# READ - Get all items
@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(list(inventory.values())), 200


# UPDATE - Update item quantity
@app.route("/inventory/<int:item_id>", methods=["PUT"])
def update_inventory(item_id):
    # Check if item exists
    if item_id not in inventory:
        return jsonify({"error": "Item doesn't exist"}), 404

    data = request.json

    # Validate quantity
    if "quantity" not in data:
        return jsonify({"error": "Quantity field required"}), 400
    
    if not isinstance(data["quantity"], int):
        return jsonify({"error": "Quantity must be integer"}), 400
    
    if data["quantity"] < 0:
        return jsonify({"error": "Quantity cannot be negative"}), 400

    # Update quantity
    inventory[item_id]["quantity"] = data["quantity"]

    return jsonify(inventory[item_id]), 200


# DELETE - Remove item (only if quantity is 0)
@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    # Check if item exists
    if item_id not in inventory:
        return jsonify({"error": "Item not found"}), 404

    # Business rule: Can't delete if quantity remains
    if inventory[item_id]["quantity"] > 0:
        return jsonify({
            "error": "Cannot delete item with remaining quantity",
            "current_quantity": inventory[item_id]["quantity"]
        }), 409

    # Delete item
    del inventory[item_id]
    
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)