from flask import Blueprint, request, jsonify
from models.db import mysql
import bcrypt
import jwt
import datetime
from flask import current_app

auth_bp = Blueprint('auth', __name__)

# Signup
@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', 'member')

    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO users (name, email, password, role) VALUES (%s, %s, %s, %s)",
        (name, email, hashed_pw, role)
    )
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "User registered successfully"})


# Login
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE email=%s", (email,))
    user = cur.fetchone()
    cur.close()

    if user:
        stored_password = user[3]

        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):

            token = jwt.encode({
                'user_id': user[0],
                'role': user[4],
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
            }, current_app.config['SECRET_KEY'], algorithm="HS256")

            return jsonify({
                "message": "Login successful",
                "token": token
            })

    return jsonify({"error": "Invalid credentials"}), 401