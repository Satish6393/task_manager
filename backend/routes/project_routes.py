from flask import Blueprint, request, jsonify
from models.db import mysql
from routes.protected_routes import token_required

project_bp = Blueprint('projects', __name__)

# ✅ Create Project (Admin only)
@project_bp.route('/projects', methods=['POST'])
@token_required
def create_project():
    user = request.user

    if user['role'] != 'admin':
        return jsonify({"error": "Only admin can create project"}), 403

    data = request.get_json()
    name = data.get('name')

    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO projects (name, created_by) VALUES (%s, %s)",
        (name, user['user_id'])
    )
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Project created successfully"})


# ✅ Get All Projects
@project_bp.route('/projects', methods=['GET'])
@token_required
def get_projects():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM projects")
    projects = cur.fetchall()
    cur.close()

    return jsonify({"projects": projects})