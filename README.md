# Inventory Management API

A structured REST API built using Flask and MySQL to manage inventory items.

This project implements full CRUD operations with validation, business rules, and a clean layered backend architecture.

---

## Features

* Create inventory items
* Get all items
* Get item by ID
* Update item name and quantity (partial updates supported)
* Delete item (only if quantity is 0)
* Input validation (fields, types, constraints)
* Proper HTTP status codes
* MySQL database integration
* Layered architecture (routes, service, storage)

---

## Tech Stack

* Python 3.12.3
* Flask
* MySQL
* mysql-connector-python
* Virtual environment (venv)

---

## Project Structure

inventory_management_api/

-- app/
---- **init**.py
---- routes.py      (handles HTTP requests)
---- service.py     (business logic)
---- storage.py     (database operations)

-- inventory_management_api.py  (entry point)
-- requirements.txt
-- .gitignore
-- README.md

---

## Setup Instructions

1. Clone repository

git clone https://github.com/jyothi-basu/inventory-management-api.git
cd inventory-management-api

---

2. Create virtual environment

python3 -m venv venv

---

3. Activate environment

Windows
venv\Scripts\activate

Linux / macOS / WSL
source venv/bin/activate

---

4. Install dependencies

pip install -r requirements.txt

---

5. Setup MySQL database

Login to MySQL:

mysql -u root -p

Create database:

CREATE DATABASE inventory_management_db;
USE inventory_management_db;

Create table:

CREATE TABLE items (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255) NOT NULL UNIQUE,
quantity INT NOT NULL
);

---

6. Run application

python inventory_management_api.py

Server runs at:
http://127.0.0.1:5000/

---

## API Endpoints

Create item
POST /inventory

Body
{
"name": "Keyboard",
"quantity": 10
}

---

Get all items
GET /inventory

---

Get item by ID
GET /inventory/<item_id>

---

Update item
PUT /inventory/<item_id>

Body (partial or full)
{
"name": "Mouse",
"quantity": 5
}

---

Delete item
DELETE /inventory/<item_id>

Condition

* Item must exist
* Quantity must be 0

---

## Validation Rules

* Only allowed fields: name, quantity
* Name must be a non-empty string
* Item name must be unique (duplicate entries are not allowed. Duplicate item creation returns 409 Conflict)
* Quantity must be a non-negative integer
* Invalid fields are rejected
* Request body must be valid JSON

---

## HTTP Status Codes

200 OK
201 Created
204 No Content
400 Bad Request
404 Not Found
409 Conflict

---

## Architecture

Routes layer
Handles HTTP requests and basic validation

Service layer
Handles business logic and rules

Storage layer
Handles database queries (MySQL)

---

## Current Limitations

* No authentication system
* Single-user system (no roles/permissions)
* No deployment (runs locally)

---

## Next Improvements

* Add authentication (admin/user roles)
* Deploy API (Render / cloud)
* Add database migrations
* Add automated tests

---

## Notes

* Sensitive data like database password should not be committed
* Use environment variables for credentials (recommended)
* client.http can be used for API testing

---

## Author

Jyothi Basu

---

## License

This project is created for learning and skill development.
