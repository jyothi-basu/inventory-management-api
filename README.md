# Inventory Management API

A RESTful API built with Flask for managing inventory items.

This project implements full CRUD (Create, Read, Update, Delete) operations with input validation and business rule enforcement. The API stores data in memory and returns structured JSON responses.

---

## Features

- Create inventory items
- Retrieve all inventory items
- Retrieve a specific item by ID
- Update item quantity
- Delete item (only when quantity is 0)
- Input validation with proper HTTP status codes
- Business rule enforcement using 409 Conflict

---

## Tech Stack

- Python 3.14
- Flask 3.x
- Virtual environment (venv)
- RESTful API design principles

---

## Installation and Setup

1. Clone the repository:

   git clone https://github.com/jyothi-basu/inventory-management-api.git

2. Navigate into the project folder:

   cd inventory-api

3. Create a virtual environment:

   python -m venv venv

4. Activate the virtual environment:

   Windows:
   venv\Scripts\activate

   macOS/Linux:
   source venv/bin/activate

5. Install dependencies:

   pip install -r requirements.txt

6. Run the application:

   python app.py

The server will start at:

   http://127.0.0.1:5000/

---

## API Endpoints

### Create Item

POST /inventory

Request Body:
{
  "name": "Keyboard",
  "quantity": 10
}

Response:
201 Created
{
  "id": 1,
  "name": "Keyboard",
  "quantity": 10
}

Validation Errors:
400 Bad Request

---

### Get All Items

GET /inventory

Response:
200 OK
[
  {
    "id": 1,
    "name": "Keyboard",
    "quantity": 10
  }
]

---

### Get Single Item

GET /inventory/<item_id>

Response:
200 OK
{
  "id": 1,
  "name": "Keyboard",
  "quantity": 10
}

If item does not exist:
404 Not Found

---

### Update Item Quantity

PUT /inventory/<item_id>

Request Body:
{
  "quantity": 5
}

Response:
200 OK
{
  "id": 1,
  "name": "Keyboard",
  "quantity": 5
}

Validation Errors:
400 Bad Request

If item does not exist:
404 Not Found

---

### Delete Item

DELETE /inventory/<item_id>

Successful Response:
204 No Content

If item does not exist:
404 Not Found

If quantity is greater than 0:
409 Conflict
{
  "error": "Cannot delete item with remaining quantity",
  "current_quantity": 5
}

---

## Validation Rules

- Name must be a non-empty string
- Quantity must be a non-negative integer
- JSON body must contain required fields
- Items with quantity greater than zero cannot be deleted

---

## Project Structure

The repository contains:

- app.py  
  Main Flask application containing all routes and logic.

- requirements.txt  
  Python dependencies.

- README.md  
  Project documentation.

---

## Notes

- Data is stored in memory (dictionary).
- Restarting the server resets all inventory data.
- This project focuses on CRUD operations, validation, and HTTP status handling.
