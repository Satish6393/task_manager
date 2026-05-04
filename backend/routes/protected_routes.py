from flask import Blueprint, jsonify, request
from utils.auth_middleware import token_required
from models.db import mysql
from datetime import date

protected_bp = Blueprint('protected', __name__)

@protected_bp.route('/dashboard', methods=['GET'])
@token_required
def dashboard():
    user = request.user
    cur = mysql.connection.cursor()

    # Role-based filtering
    if user['role'] == 'admin':
        cur.execute("SELECT COUNT(*) FROM tasks")
        total = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM tasks WHERE status='done'")
        completed = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM tasks WHERE status='pending'")
        pending = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM tasks WHERE deadline < %s AND status!='done'", (date.today(),))
        overdue = cur.fetchone()[0]

    else:
        uid = user['user_id']

        cur.execute("SELECT COUNT(*) FROM tasks WHERE assigned_to=%s", (uid,))
        total = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM tasks WHERE assigned_to=%s AND status='done'", (uid,))
        completed = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM tasks WHERE assigned_to=%s AND status='pending'", (uid,))
        pending = cur.fetchone()[0]

        cur.execute("""
            SELECT COUNT(*) FROM tasks 
            WHERE assigned_to=%s AND deadline < %s AND status!='done'
        """, (uid, date.today()))
        overdue = cur.fetchone()[0]

    cur.close()

    return jsonify({
        "total_tasks": total,
        "completed": completed,
        "pending": pending,
        "overdue": overdue
    })