# prou_full-stack
# Employee Task Manager

A full-stack web application to manage employees and their tasks.  
This project includes a REST API built with FastAPI and a React-based frontend.

---

## 1. Tech Stack

- **Frontend:** React, Vite, HTML, CSS, JavaScript
- **Backend:** FastAPI (Python)
- **Database:** SQLite (via SQLAlchemy)

---

## 2. Features

### Backend (API)
- Employee management: create, read, update, delete
- Task management: create, read, update, delete
- Assign tasks to employees
- Filter tasks by status and employee
- SQLite database with SQLAlchemy ORM
- CORS configured for local frontend

### Frontend (Web App)
- Dashboard view of employees and tasks
- Create, update, delete employees
- Create, update, delete tasks
- Set task status (TODO / IN_PROGRESS / DONE)
- Assign tasks to employees
- Responsive layout with simple, clean UI

---

## 3. Getting Started

### 3.1. Prerequisites

- Python 3.9+
- Node.js 18+ and npm

---

## 4. Backend Setup

```bash
cd backend
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API will be available at:  
`http://localhost:8000`

Interactive API docs (Swagger UI):  
`http://localhost:8000/docs`

The SQLite database file `app.db` will be created automatically in the backend folder.

---

## 5. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Vite will show a local URL (typically `http://localhost:5173`).  
Open it in the browser.

The frontend is configured to talk to the backend at `http://localhost:8000/api`.

---

## 6. API Overview

Base URL: `http://localhost:8000/api`

### Employees

- `GET /employees` – list employees
- `GET /employees/{id}` – get one employee
- `POST /employees` – create employee
- `PUT /employees/{id}` – update employee
- `DELETE /employees/{id}` – delete employee
- `GET /employees/{id}/tasks` – list tasks for a given employee

### Tasks

- `GET /tasks` – list tasks (with optional filters)
- `GET /tasks/{id}` – get one task
- `POST /tasks` – create task
- `PUT /tasks/{id}` – update task
- `DELETE /tasks/{id}` – delete task

---



## 7. Assumptions

- Each task is assigned to exactly one employee.
- Authentication and authorization are not implemented (for clarity and focus on CRUD).
- Roles are informational only (e.g., "Developer", "Manager").

---

## 8. Bonus Ideas

- Add authentication
- Add pagination and sorting
- Add task priority
- Add search by name or email
