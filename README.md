Here’s the content formatted for your `README.md` file:

---

# Weekly Schedule API

This Django project implements a simple CRUD API for managing weekly schedules with time slots for each day of the week. The API is documented with Swagger (drf-spectacular), and it uses JWT authentication for secure access.

## Features

- Create, Read, Update, and Delete (CRUD) weekly schedules.
- JWT-based authentication for API access.
- Swagger documentation to explore the API endpoints.
- Unit tests to validate functionality.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Virtualenv (recommended)

### Setup Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/shabeebhasan/schedule_django.git
   cd schedule_django
   ```

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   You may want to set environment variables for sensitive settings like secret keys, database credentials, etc.

5. **Run database migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional)**

   If you want to access the Django admin panel, create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

8. **Access Swagger UI**

   You can access the Swagger UI to explore the API endpoints at:

   ```
   http://127.0.0.1:8000/swagger/
   ```

## Running Tests

To run the unit tests, use the following command:

```bash
python manage.py test
```

## JWT Authentication

This API uses JWT (JSON Web Token) authentication for secure access. You can get an access token by sending a `POST` request to the following endpoint with valid credentials:

```
POST /api/token/
```

Example:

```json
{
    "username": "admin",
    "password": "admin"
}
```

This will return an access token which can be used in the `Authorization` header with the `Bearer` prefix for subsequent API requests:

```
Authorization: Bearer your_access_token
```

## Requirements

All the project dependencies are listed in `requirements.txt`. To install them, simply run:

```bash
pip install -r requirements.txt
```

## API Endpoints

- `GET /api/weekly-schedules/` - List all weekly schedules.
- `POST /api/weekly-schedules/` - Create a new weekly schedule.
- `GET /api/weekly-schedules/{id}/` - Retrieve a specific weekly schedule.
- `PUT /api/weekly-schedules/{id}/` - Update an existing weekly schedule.
- `DELETE /api/weekly-schedules/{id}/` - Delete a weekly schedule.

## Running Swagger with Authentication

Once logged in with a JWT token, Swagger UI can be accessed via:

```
http://127.0.0.1:8000/swagger/
```

Use the token in the "Authorize" button on the Swagger page to make authenticated requests.
