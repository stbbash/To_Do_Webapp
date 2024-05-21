# To_Do Webapp

This is a To_Do Webapp implemented with the Django web framework, enhanced to make use of the Django REST Framework (DRF) API. Every Python package installation was done in a virtual environment (`vbash`). The app includes CORS configuration, allowing URLs from all origins to perform READ, UPDATE, and DELETE (CRUD) operations on the API's data. Additionally, the app is designed to accept JSON format on the URLs.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)

## Features

- Create, Read, Update, and Delete (CRUD) operations for to-do tasks.
- RESTful API built with Django REST Framework.
- CORS configuration allowing access from all origins.
- JSON format support for API endpoints.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/to_do_webapp.git
   cd to_do_webapp
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv vbash
   source vbash/bin/activate   # On Windows, use `vbash\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## Usage

### API Endpoints

- **List all tasks:**
  ```http
  GET /api/user/
  ```

- **Create a new task:**
  ```http
  POST /api/user/create
  ```

- **Retrieve a specific task:**
  ```http
  GET /api/user/<user_id>/
  ```

- **Update a specific task:**
  ```http
  PUT /api/user/<user_id>/<id>/update
  ```

- **Delete a specific task:**
  ```http
  DELETE /api/user/<user_id>/<id>/delete
  ```

### JSON Format Support

The API endpoints accept and return data in JSON format. Ensure that the `Content-Type` header is set to `application/json` when making requests.

## Screenshots

- **REST API Overview:**

- **To-Do Details:**

- **Login Page:**

- **Register Page:**

- **To-Do Tasks:**

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.
