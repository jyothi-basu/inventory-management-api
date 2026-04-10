# Inventory Management API

A production-style REST API built using Flask and MySQL for managing inventory items, with secure authentication and route protection. Built and debugged in a Linux (WSL) environment with real-world deployment-style setup.

This project demonstrates backend engineering concepts including layered architecture, validation, authentication, and debugging.

---

## Features

### Inventory Management
- Create inventory items
- Get all items
- Get item by ID
- Update item (partial updates supported)
- Delete item (only if quantity is 0)

### Authentication & Security
- User signup with password hashing (bcrypt)
- User login with credential verification
- JWT-based authentication
- Protected routes using token validation
- Secure password storage (no plain text passwords)

### System Design
- Layered architecture (Routes → Service → Storage)
- Input validation and error handling
- Proper HTTP status codes
- MySQL database integration

---

## Tech Stack

- Python 3.12
- Flask
- MySQL
- mysql-connector-python
- bcrypt
- PyJWT
- Gunicorn

---

## Project Structure
inventory_management_api/
inventory_management_api.py
schema.sql
requirements.txt
README.md
.gitignore
app/
init.py
routes.py
auth.py
decorators.py
service.py
storage.py

---

## Setup Instructions

### 1. Clone repository
git clone https://github.com/jyothi-basu/inventory-management-api.git
cd inventory-management-api

---

### 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

---

### 3. Install dependencies
pip install -r requirements.txt

---

### 4. Set environment variables
export SECRET_KEY="your_secret_key"
export DB_PASSWORD="your_db_password"

> DB_PASSWORD is used for MySQL connection in the storage layer.

---

### 5. Setup database
mysql -u root -p < schema.sql

---

### 6. Run application

#### Development
export FLASK_APP=inventory_management_api.py
flask run


#### Production-style (recommended)
gunicorn -w 4 -b 127.0.0.1:5000 inventory_management_api:app

---

Server runs at:
http://127.0.0.1:5000/

---

## Authentication Flow

1. User signs up → password is hashed using bcrypt  
2. User logs in → password is verified  
3. Server generates JWT token  
4. Client sends token in header:
Authorization: Bearer <token>

5. Protected routes validate token before execution  

---

## API Endpoints

### Authentication

**POST /signup**
{
"name": "User",
"email": "user@gmail.com",
"password": "password123"
}

---

**POST /login**
{
"email": "user@gmail.com",
"password": "password123"
}

Returns JWT token.

---

### Inventory (Protected Routes)

All routes require:
Authorization: Bearer <token>

---

**POST /inventory**  
Create item  

---

**GET /inventory**  
Get all items  

---

**GET /inventory/<id>**  
Get item by ID  

---

**PUT /inventory/<id>**  
Update item  

---

**DELETE /inventory/<id>**  
Delete item (only if quantity = 0)  

---

## Validation Rules

- Name must be a non-empty string  
- Email must be unique  
- Password must be non-empty  
- Quantity must be a non-negative integer  
- Invalid fields are rejected  

---

## HTTP Status Codes

- 200 OK  
- 201 Created  
- 204 No Content  
- 400 Bad Request  
- 401 Unauthorized  
- 404 Not Found  
- 409 Conflict  

---

## Architecture

- Routes layer → handles HTTP requests  
- Service layer → business logic & authentication  
- Storage layer → database operations  

---

## .gitignore

The project uses a Python-based `.gitignore` to exclude:

- `venv/` (virtual environment)
- `__pycache__/` (compiled Python files)
- local testing files (e.g., client.http )
- environment-specific files

This ensures sensitive and unnecessary files are not committed.

---

## Future Improvements

- Role-based authorization (admin/user)
- Deployment (Render / VPS)
- Database migrations
- Automated testing

---

## Notes

- Environment variables are used for sensitive data
- Database credentials are not stored in code
- Tested using REST client
- Developed and tested in WSL environment

---

## Author

Jyothi Basu

---

## License

This project is created for learning and demonstration purposes.
