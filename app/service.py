from app import storage

# Create new item:
def create_item(data):
    if data["name"].strip() == "":
        return {"error": "Name cannot be empty"}, 400

    if data["quantity"] < 0:
        return {"error": "Quantity cannot be negative"}, 400

    item = storage.create_item(data["name"], data["quantity"])
    return item, 201

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

    if item[item_id]["quantity"] > 0:
        return {
            "error": "Cannot delete item with remaining quantity",
            "current_quantity": item[item_id]["quantity"]
        }, 409

    storage.delete_item(item_id)
    return {}, 204