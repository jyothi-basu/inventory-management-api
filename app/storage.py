# Inventory data storage
inventory = {}
next_id = 1

# create new item:
def create_item(name, quantity):
    global next_id

    item = {
        "id": next_id,
        "name": name,
        "quantity": quantity
    }

    inventory[next_id] = item
    next_id += 1
    return item

# Get a specific item:
def get_item(item_id):
    item = inventory.get(item_id)
    return item

# Get all items:
def get_inventory():
    return list(inventory.values())


# Update item:
def update_item(item_id, updates):
    item = inventory.get(item_id)

    if not item:
        return None

    item.update(updates)
    return item


# Delete item:
def delete_item(item_id):
    return inventory.pop(item_id, None)
    return ""