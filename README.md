# Team Task Manager (Full-Stack Web Application)

## Project Overview

Team Task Manager is a full-stack web application that allows teams to manage projects, assign tasks, and track progress efficiently. The system includes role-based access control (Admin & Member), secure authentication, and a dashboard for monitoring task status.

---

## Features

### Authentication

* User Signup & Login
* Password hashing using bcrypt
* JWT-based authentication

### Role-Based Access Control

* **Admin**

  * Create projects
  * Assign tasks to users
  * View all tasks
* **Member**

  * View assigned tasks only
  * Update task status

### Project Management

* Create and manage projects
* Link tasks to specific projects

### Task Management

* Create tasks with deadlines
* Assign tasks to team members
* Update task status (Pending / In Progress / Done)

### Dashboard

* Total tasks
* Completed tasks
* Pending tasks
* Overdue tasks

---

## Tech Stack

### Backend

* Python (Flask)
* MySQL
* REST APIs
* JWT Authentication

### Frontend

* HTML
* CSS
* JavaScript

### Tools & Deployment

* Postman (API Testing)
* GitHub (Version Control)
* Railway (Deployment)

---

## Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/https://github.com/Satish6393/task_manager/task-manager.git
cd task-manager/backend
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Database (MySQL)

Create database:

```sql
CREATE DATABASE task_manager;
```

### 5️⃣ Configure Environment Variables

Update `config.py`:

```python
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "yourpassword"
MYSQL_DB = "task_manager"
SECRET_KEY = "your_secret_key"
```

### 6️⃣ Run the Application

```bash
python app.py
```

---

## API Endpoints

### Auth

* `POST /api/auth/signup`
* `POST /api/auth/login`

### Projects

* `POST /api/projects` (Admin)
* `GET /api/projects`

### Tasks

* `POST /api/tasks` (Admin)
* `GET /api/tasks`
* `PUT /api/tasks/<id>`

### Dashboard

* `GET /api/dashboard`

---

##  Live Demo

[Live Application URL](#) *(Add Railway link here)*

---

## Demo Video

[Demo Video Link](#)

---

## Future Improvements

* UI enhancement with React
* Notifications system
* Email alerts for deadlines
* Team collaboration features

---

## Author

**Satish Singh**
B.Tech (AI & ML)
Skills: Python, Flask, SQL, Data Analytics, PowerBI

---

## Conclusion

This project demonstrates full-stack development skills including backend API design, database management, authentication, and deployment. It is built following industry-level practices and is scalable for real-world applications.
