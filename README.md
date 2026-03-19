# Inventory Management API

A structured REST API built using Flask to manage inventory items.

This project implements CRUD operations with validation, business rules, and a layered backend architecture.

---

## Features

* Create inventory items
* Get all items
* Get item by ID
* Update item name and quantity
* Delete item (only if quantity is 0)
* Input validation
* Proper HTTP status codes
* Layered architecture

---

## Tech Stack

* Python 3.12.3
* Flask
* Virtual environment (venv)

---

## Project Structure

inventory_management_api/

-- app/
---- **init**.py
---- routes.py      (handles HTTP requests)
---- service.py     (business logic)
---- storage.py     (data storage)

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

5. Run application

python inventory_management_api.py

Server runs at
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
Item must exist
Quantity must be 0

---

## Validation Rules

* Name must be non-empty string
* Quantity must be non-negative integer
* Request body must be valid JSON
* Cannot delete item if quantity > 0

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
Handles HTTP requests and validation

Service layer
Handles business logic

Storage layer
Handles data storage

---

## Current Limitations

* Data stored in memory
* Data resets on server restart
* No authentication system

---

## Next Improvements

* Add database (SQLite, PostgreSQL)
* Add authentication (admin and user roles)
* Add persistent storage
* Add tests

---

## Notes

* venv, **pycache**, and .pyc files are ignored
* client.http is used for API testing

---

## Author

Jyothi Basu

---

## License

This project is created for learning and skill development.
