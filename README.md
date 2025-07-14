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
### 2.Create and activate virtual environment:
```
bash

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```
### 3.Install dependencies:

`pip install -r requirements.txt`  
### 4.Configure PostgreSQL:

Set up a PostgreSQL database and user.

Add your DB credentials to .env or directly in settings.py.

### 5.Run migrations:

`python manage.py migrate`

### 6.Start development server:

`python manage.py runserver`


## 🛠️ Tech Stack
Backend: Django, Django REST Framework

Database: PostgreSQL

Tools: Postman, SwaggerHub (reference only)

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