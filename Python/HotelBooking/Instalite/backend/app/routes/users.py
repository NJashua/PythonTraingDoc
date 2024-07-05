# app/routes/users.py
from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

users_bp = Blueprint('users', __name__)

user_service = UserService()

@users_bp.route('/users', methods=['GET'])
def get_users():
    users = user_service.get_users()
    return jsonify([user.to_dict() for user in users])

@users_bp.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = user_service.get_user(username)
    if user:
        return jsonify(user.to_dict())
    return jsonify({'error': 'User not found'}), 404

@users_bp.route('/users/<username>/posts', methods=['GET'])
def get_user_posts(username):
    user = user_service.get_user(username)
    if user:
        posts = user_service.get_posts(user.id)
        return jsonify([post.to_dict() for post in posts])
    return jsonify({'error': 'User not found'}), 404

@users_bp.route('/users/<username>/followers', methods=['GET'])
def get_user_followers(username):
    user = user_service.get_user(username)
    if user:
        followers = user_service.get_followers(user.id)
        return jsonify([follower.to_dict() for follower in followers])
    return jsonify({'error': 'User not found'}), 404

@users_bp.route('/users/<username>/following', methods=['GET'])
def get_user_following(username):
    user = user_service.get_user(username)
    if user:
        following = user_service.get_following(user.id)
        return jsonify([follow.to_dict() for follow in following])
    return jsonify({'error': 'User not found'}), 404