# Inventory data storage
import mysql.connector
import os

# Database password:
DB_PASSWORD = os.getenv("DB_PASSWORD")
# create connection function
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password= DB_PASSWORD,
        database="inventory_management_db"
    )


# create new item:
def create_item(name, quantity):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "INSERT INTO items (name, quantity) VALUES (%s, %s)"
    cursor.execute(query, (name, quantity))
    conn.commit()

    item = {
        "id": cursor.lastrowid,
        "name": name,
        "quantity": quantity
    }

    cursor.close()
    conn.close()

    return item


# Get a specific item:
def get_item(item_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM items WHERE id = %s"
    cursor.execute(query, (item_id,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result


# Get all items:
def get_inventory():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM items"
    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result


# Update item:
def update_item(item_id, data):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    fields = []
    values = []

    for key in data.keys():
        fields.append(f"{key} = %s")
        values.append(data[key])

    values.append(item_id)

    query = f"UPDATE items SET {', '.join(fields)} WHERE id = %s"
    cursor.execute(query, tuple(values))
    conn.commit()

    updated_item = get_item(item_id)

    cursor.close()
    conn.close()

    return updated_item


# Delete item:
def delete_item(item_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "DELETE FROM items WHERE id = %s"
    cursor.execute(query, (item_id,))
    conn.commit()

    cursor.close()
    conn.close()

# Create new user:
def signup(name, email, hashed_password):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        query = "INSERT INTO users(name, email, password_hash) VALUES(%s, %s, %s)"
        cursor.execute(query, (name, email, hashed_password))
        conn.commit()

        return {"message": "User created successfully"}, 201

    except Exception as e:
        return {"error": str(e)}, 400

    finally:
        conn.close()
        cursor.close()

# User login:
def login(email):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    user = cursor.fetchone()
    conn.close()
    cursor.close()

    return user