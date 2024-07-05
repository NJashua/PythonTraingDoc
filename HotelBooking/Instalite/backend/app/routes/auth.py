# app/routes/auth.py
from flask import Blueprint, request, jsonify
from app.services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    if AuthService().login(username, password):
        return jsonify({'message': 'Logged in successfully'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@auth_bp.route('/register', methods=['POST'])
def register():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    user = AuthService().register(username, email, password)
    return jsonify({'message': 'User created successfully'}), 201

@auth_bp.route('/logout', methods=['POST'])
def logout():
    AuthService().logout()
    return jsonify({'message': 'Logged out successfully'}), 200