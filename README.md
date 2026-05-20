# Inventory Management API

A Flask REST API for managing inventory items with MySQL persistence, JWT authentication, role-based authorization, password hashing, protected routes, validation, and a layered backend structure.

The project was built as a backend learning project and evolved through clear milestones: single-file CRUD, layered architecture, MySQL integration, authentication with protected routes, deployment, and role-based authorization.

---

## Live API

Base URL: `https://inventory-management-api-4ikv.onrender.com`

Deployment stack:
- Flask API hosted on Render
- MySQL database hosted on alwaysdata
- Configuration managed through environment variables

> Note: The API is hosted on Render free tier, so the first request after inactivity may take some time to wake up.

---

## Features

### Inventory Management
- Create inventory items
- Get all inventory items
- Get item by ID
- Update item with partial update support
- Delete item only when quantity is `0`

### Authentication & Security
- User signup
- User login
- Password hashing with bcrypt
- JWT token generation
- Protected inventory routes
- Role-based authorization with `admin` and `staff` roles
- Secure password storage without plain text passwords

### Backend Design
- Layered architecture: routes, service, storage, authentication
- MySQL database integration
- Input validation
- Error handling with proper HTTP status codes
- Environment-based configuration for secrets and database credentials
- Deployment-ready Gunicorn setup

---

## Tech Stack

- Python 3.12
- Flask
- MySQL
- mysql-connector-python
- bcrypt
- PyJWT
- Gunicorn
- Git and GitHub
- Linux/WSL development environment

---

## Project Structure

```text
inventory-management-api/
|-- inventory_management_api.py
|-- schema.sql
|-- requirements.txt
|-- README.md
|-- .gitignore
|-- .env.example
`-- app/
    |-- __init__.py
    |-- routes.py
    |-- auth.py
    |-- decoraters.py
    |-- service.py
    `-- storage.py
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/jyothi-basu/inventory-management-api.git
cd inventory-management-api
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

The required variables are documented in `.env.example`.

```bash
export SECRET_KEY="your_secret_key"
export DB_HOST="localhost"
export DB_USER="your_database_user"
export DB_PASSWORD="your_database_password"
export DB_NAME="inventory_management_db"
export DB_PORT="3306"
```

Do not commit a real `.env` file. It may contain database credentials and secret keys.

### 5. Set Up Database

Create a MySQL database first, then run the schema inside that database:

```bash
mysql -u your_database_user -p your_database_name < schema.sql
```

For a remote database:

```bash
mysql -h your_database_host -P 3306 -u your_database_user -p your_database_name < schema.sql
```

### 6. Run Application

Development:

```bash
export FLASK_APP=inventory_management_api.py
flask run
```

Production-style local run:

```bash
gunicorn -w 1 -b 127.0.0.1:5000 inventory_management_api:app
```

Local server:

```text
http://127.0.0.1:5000/
```

---

## Deployment Notes

For platforms such as Render, configure these environment variables in the platform dashboard:

- `SECRET_KEY`
- `DB_HOST`
- `DB_USER`
- `DB_PASSWORD`
- `DB_NAME`
- `DB_PORT`

Recommended Render start command:

```bash
gunicorn --bind 0.0.0.0:$PORT inventory_management_api:app
```

For hosted MySQL databases, run `schema.sql` inside the database provided by the hosting platform.

---

## Authentication Flow

1. User signs up with name, email, and password.
2. Password is hashed using bcrypt.
3. User logs in with email and password.
4. Server generates a JWT token.
5. Client sends the token in the request header:

```http
Authorization: Bearer <token>
```

6. Protected routes validate the token and check the user's role before processing the request.

New users are assigned the `staff` role by default. Admin users should be promoted manually in the database.

Current limitation: JWT tokens do not yet include an expiration time.

---

## Role-Based Authorization

The API uses two roles:

- `admin`
- `staff`

Recommended admin promotion query:

```sql
UPDATE users
SET role = 'admin'
WHERE email = 'your_email@example.com';
```

Route permissions:

| Method | Endpoint | Admin | Staff |
|---|---|---:|---:|
| `POST` | `/inventory` | Yes | No |
| `GET` | `/inventory` | Yes | Yes |
| `GET` | `/inventory/<id>` | Yes | Yes |
| `PUT` | `/inventory/<id>` | Yes | Yes |
| `DELETE` | `/inventory/<id>` | Yes | No |

Requests with a missing or invalid token return `401 Unauthorized`. Requests with a valid token but insufficient role permission return `403 Forbidden`.

---

## API Endpoints

### Health Check

```http
GET /
```

Response:

```json
{
  "message": "Inventory API running"
}
```

### Signup

```http
POST /signup
```

Request body:

```json
{
  "name": "User",
  "email": "user@gmail.com",
  "password": "password123"
}
```

### Login

```http
POST /login
```

Request body:

```json
{
  "email": "user@gmail.com",
  "password": "password123"
}
```

Returns a JWT token.

### Inventory Routes

All inventory routes require:

```http
Authorization: Bearer <token>
```

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/inventory` | Create item |
| `GET` | `/inventory` | Get all items |
| `GET` | `/inventory/<id>` | Get item by ID |
| `PUT` | `/inventory/<id>` | Update item |
| `DELETE` | `/inventory/<id>` | Delete item only if quantity is `0` |

Example create item request:

```json
{
  "name": "Keyboard",
  "quantity": 10
}
```

---

## Validation Rules

- Name must be a non-empty string
- Email must be unique
- Password must be non-empty
- Quantity must be a non-negative integer
- Invalid fields are rejected
- Items with quantity greater than `0` cannot be deleted

---

## HTTP Status Codes

- `200 OK`
- `201 Created`
- `204 No Content`
- `400 Bad Request`
- `401 Unauthorized`
- `403 Forbidden`
- `404 Not Found`
- `409 Conflict`

---

## Architecture

```text
Routes layer
    |
    v
Service layer
    |
    v
Storage layer
    |
    v
MySQL database
```

- Routes layer handles HTTP requests and responses.
- Service layer contains business logic and validation.
- Storage layer handles database operations.
- Authentication logic handles signup, login, JWT creation, and route protection.

---

## Release Milestones

- `v0.1.0`: Single-file Flask CRUD API with in-memory storage
- `v0.2.0`: Layered architecture refactor
- `v0.3.0`: MySQL database integration
- `v1.0.0`: JWT authentication and protected inventory routes
- `v1.1.0`: Deployment configuration and documentation overhaul
- `v1.2.0`: Role-based authorization with admin and staff permissions

---

## Notes

- Environment variables are used for sensitive configuration.
- Database credentials are not stored in code.
- `.env.example` documents required configuration values.
- New users receive the `staff` role by default.
- Developed and tested in a Linux/WSL environment.

---

## Future Improvements

- Add JWT expiration
- Add automated tests with pytest
- Add database migrations
- Add Docker-based local setup

---

## Author

Jyothi Basu

---

## License

This project is created for learning and demonstration purposes.
