# Inventory data storage
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="inventory_management_db"
)

cursor = connection.cursor(dictionary=True)


# create new item:
def create_item(name, quantity):
    query = "INSERT INTO items (name, quantity) VALUES (%s, %s)"

    cursor.execute(query, (name, quantity))
    connection.commit()

    return {
        "id": cursor.lastrowid,
        "name": name,
        "quantity": quantity
    }


# Get a specific item:
def get_item(item_id):
    query = "SELECT * FROM items WHERE id = %s"
    cursor.execute(query, (item_id,))
    return cursor.fetchone()


# Get all items:
def get_inventory():
    query = "SELECT * FROM items"
    cursor.execute(query)
    return cursor.fetchall()


# Update item:
def update_item(item_id, data):
    fields = []
    values = []

    for key in data.keys():
        fields.append(f"{key} = %s")
        values.append(data[key])

    values.append(item_id)
    query = f"UPDATE items SET {', '.join(fields)} WHERE id = %s"
    cursor.execute(query, tuple(values))
    connection.commit()
    return get_item(item_id)






# Delete item:
def delete_item(item_id):
    query = "DELETE FROM items WHERE id = %s"
    cursor.execute(query, (item_id))
    connection.commit()