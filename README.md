# My Django App for Vention Company.

This Django application provides a simple task management system, allowing users to create, view, update, and delete tasks organized by categories.

## Requirements:
    - Python 3.8 or newer
    - Docker (optional, for containerized deployment)
    
## Instruction:
1. Download the repository.
2. Set up a virtual environment: 'python -m venv venv' and then '.\venv\Scripts\activate' - for Windows
3. Apply migrations to create the database: 'python manage.py migrate'
4. Create a superuser: 'python manage.py createsuperuser'
5. Run the server: 'python manage.py runserver' - http://127.0.0.1:8000/
6. 'docker-compose up --build' (ensure you have Docker installed)


## The application provides the following RESTful API endpoints:

Tasks

  - List Tasks: GET /api/tasks/
  - Create Task: POST /api/tasks/ with payload { "title": "Task Title", "description": "Task Description", "category": "CategoryID", "completed": false }
  - Retrieve Task: GET /api/tasks/<id>/
  - Update Task: PUT /api/tasks/<id>/ with payload { "title": "New Title", "description": "New Description", "category": "CategoryID", "completed": true }
  - Delete Task: DELETE /api/tasks/<id>/

Categories

  - List Categories: GET /api/categories/
  - Create Category: POST /api/categories/ with payload { "name": "Category Name" }
  - Retrieve Category: GET /api/categories/<id>/
  - Update Category: PUT /api/categories/<id>/ with payload { "name": "New Category Name" }
  - Delete Category: DELETE /api/categories/<id>/

## Authentication - The API uses Token Authentication.
