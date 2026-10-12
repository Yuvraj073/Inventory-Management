# Inventory-Management

> **Project Status:** 🚧 Under Development

A beginner-friendly REST API built with **FastAPI**, **Python**, and **SQLAlchemy**. This project focuses on learning backend development, CRUD operations, API design, request handling, and database integration.

## Features Completed

- **Product Management**
  - Get All Products
  - Get Product by ID
  - Add New Product
  - Update Product (PUT)
  - Delete Product
- **Product Search**
  - Search Products by Name
  - Case-Insensitive Search
  - Partial Name Matching
- **API Development**
  - REST API Endpoints
  - Path Parameters
  - Query Parameters
  - JSON Request and Response Handling
  - Automatic API Documentation
- **Database Setup**
  - SQLAlchemy Engine Configuration
  - Database Session Configuration
  - SQLAlchemy Model Integration
  - Automatic Table Creation

> **Note:** Product operations currently use an in-memory Python list. Database integration is configured, but the CRUD endpoints are not yet connected to persistent database queries.

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- Uvicorn
- SQLite or another database configured in `config.py`

## Project Structure

```text
.
├── main.py
├── models.py
├── config.py
├── database_models.py
└── README.md
```

## API Endpoints

### Products

- `GET /products` — Retrieve all products
- `GET /products/{id}` — Retrieve a product by ID
- `POST /products` — Add a new product
- `PUT /product?id={id}` — Update an existing product
- `DELETE /product?id={id}` — Delete a product
- `GET /products/search?name={name}` — Search products by name

## Running the Project

### Clone the Repository

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

**Windows**

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install fastapi "uvicorn[standard]" sqlalchemy
```

Install the appropriate database driver based on your database configuration.

### Run the Server

```bash
uvicorn main:app --reload
```

### Visit

```text
http://127.0.0.1:8000
```

### Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

### ReDoc Documentation

```text
http://127.0.0.1:8000/redoc
```

## Example API Request

### Search Products

**Request**

```http
GET /products/search?name=phone
```

**Response**

```json
[
  {
    "id": 1,
    "name": "Phone",
    "description": "A smartphone",
    "price": 699.99,
    "quantity": 50
  }
]
```

The response fields depend on the `Product` model defined in `models.py`.

## Upcoming Features

- Database Integration for CRUD Operations
- Persistent Product Storage
- Pagination
- Advanced Search and Filtering
- Improved HTTP Status Codes
- Request Validation and Error Handling
- Unit Testing
- Docker Support
- Deployment

## Learning Objectives

This project focuses on learning:

- REST API Development
- FastAPI Framework
- CRUD Operations
- Path and Query Parameters
- JSON Request and Response Handling
- SQLAlchemy ORM
- Database Sessions and Connections
- Backend Project Structure
- API Documentation
- Database Integration

---

**Note:** This project is actively under development. New features and improvements will be added as I continue learning FastAPI and backend development.