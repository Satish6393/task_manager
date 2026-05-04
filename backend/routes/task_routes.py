from flask import Blueprint, request, jsonify
from models.db import mysql
from routes.protected_routes import token_required
from datetime import date

task_bp = Blueprint('tasks', __name__)

# ✅ Create Task (Admin only)
@task_bp.route('/tasks', methods=['POST'])
@token_required
def create_task():
    user = request.user

    if user['role'] != 'admin':
        return jsonify({"error": "Only admin can assign tasks"}), 403

    data = request.get_json()

    title = data.get('title')
    description = data.get('description')
    project_id = data.get('project_id')
    assigned_to = data.get('assigned_to')
    deadline = data.get('deadline')

    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO tasks (title, description, project_id, assigned_to, status, deadline)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (title, description, project_id, assigned_to, 'pending', deadline))

    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Task created successfully"})


# ✅ Get Tasks (Role based)
@task_bp.route('/tasks', methods=['GET'])
@token_required
def get_tasks():
    user = request.user

    cur = mysql.connection.cursor()

    if user['role'] == 'admin':
        cur.execute("SELECT * FROM tasks")
    else:
        cur.execute("SELECT * FROM tasks WHERE assigned_to=%s", (user['user_id'],))

    tasks = cur.fetchall()
    cur.close()

    return jsonify({"tasks": tasks})


# ✅ Update Task Status
@task_bp.route('/tasks/<int:id>', methods=['PUT'])
@token_required
def update_task(id):
    user = request.user
    data = request.get_json()
    status = data.get('status')

    cur = mysql.connection.cursor()

    # Member can update only their task
    cur.execute("SELECT assigned_to FROM tasks WHERE id=%s", (id,))
    task = cur.fetchone()

    if not task:
        return jsonify({"error": "Task not found"}), 404

    if user['role'] != 'admin' and task[0] != user['user_id']:
        return jsonify({"error": "Not authorized"}), 403

    cur.execute("UPDATE tasks SET status=%s WHERE id=%s", (status, id))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Task updated"})