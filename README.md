# TodoApp
A simple Todo web application built with FastAPI, SQLAlchemy, and Alembic. It supports basic user registration, authentication, and CRUD operations for tasks.
## Features
User registration and login with hashed passwords

Create, read, update, and delete todo items

SQLite database with SQLAlchemy ORM

Database migrations using Alembic

Organized structure with routers, templates, and static files

Simple HTML interface rendered by Jinja2

## Installation and Setup
### Clone the repository
   ```bash
   git clone https://github.com/Baoying1206/TodoApp.git
   cd TodoApp
   ```
### Environment Setup
1. Create a `.env` file based on `.env.example`
2. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```
## Database Migration
Initialize and apply Alembic migrations:
   ```bash
   alembic upgrade head
   ```
If you update models:
   ```bash
   alembic revision --autogenerate -m "update models"
   alembic upgrade head
   ```
## Run the Application
Start the server:
   ```bash
   uvicorn main:app --reload
   ```
Then open the browser at:
   ```bash
   http://127.0.0.1:8000
   ```

