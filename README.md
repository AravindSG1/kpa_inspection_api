# KPA Inspection API Assignment

The APIs simulate the submission and retrieval of "Wheel Specification" form data using Django and Django REST Framework.


## 📌 APIs Implemented

### 1. Submit Wheel Specification (POST)
- **Endpoint:** `/api/forms/wheel-specifications/`
- **Method:** `POST`
- **Description:** Accepts a JSON payload to create a new wheel specification form.
- **Expected Status:** `201 Created`
- **Response:**
```
json
{
  "success": true,
  "message": "Wheel specification submitted successfully.",
  "data": {
    "formNumber": "WHEEL-2025-001",
    "submittedBy": "user_id_123",
    "submittedDate": "2025-07-03",
    "status": "Saved"
  }
}
```  

## 2.Get Filtered Wheel Specification (GET)
- **Endpoint:** /api/forms/wheel-specifications/

- **Method:** GET

- **Query Params (optional):**

    - formNumber

    - submittedBy

    - submittedDate

- **Description:** Fetches list of forms based on filters.

- **Expected Status:** 200 OK

- **Response Example:**
```
json

{
  "success": true,
  "message": "Filtered wheel specification forms fetched successfully.",
  "data": [
    {
      "formNumber": "WHEEL-2025-001",
      "submittedBy": "user_id_123",
      "submittedDate": "2025-07-03",
      "fields": {
        "treadDiameterNew": "915 (900-1000)",
        "wheelGauge": "1600 (+2,-1)"
      }
    }
  ]
}
```
## 🚀 Setup Instructions
### 1.Clone the repo:
```
bash

git clone https://github.com/yourusername/kpa-assignment.git
cd kpa-assignment
```
### 2. 🐳 Build and Start the Containers
`docker-compose up --build`  
This will:

Build the Django app container

Set up the PostgreSQL database

Apply migrations automatically

### 3. ⚙️ Environment Configuration
Update the .env file at the project root with your database and app settings:

```
POSTGRES_DB=db_name
POSTGRES_USER=db_user
POSTGRES_PASSWORD=db_user_password
DB_HOST=db
DB_PORT=5432
```

### 4. 🔁 Useful Docker Commands
Rebuild containers:
```
docker-compose down
docker-compose up --build
```
## 📘 API Documentation
This project uses drf-spectacular to auto-generate OpenAPI-compliant API documentation for the Django REST Framework.

Once the server is running, you can access the documentation at:

Endpoint	Description  
`/api/schema/`             🔧 Raw OpenAPI schema in yaml format  
`/api/docs/swagger/`	     📄 Swagger UI (interactive API explorer)  
`/api/docs/redoc/`bb       📘 ReDoc UI (alternative documentation)

These endpoints are auto-generated and kept in sync with your views and serializers.

## 🛠️ Tech Stack
Backend: Django, Django REST Framework

Database: PostgreSQL

Tools: Postman, SwaggerHub 

## ✅ Features Implemented
Create new wheel specification form

Filter and retrieve wheel specifications via GET parameters

JSONField support for dynamic input storage

Custom API response structure

Query parameter filtering

## ⚠️ Assumptions & Limitations
- No authentication has been implemented.

- Input validation is basic.

- No update (PUT) or delete (DELETE) support (not required in assignment).