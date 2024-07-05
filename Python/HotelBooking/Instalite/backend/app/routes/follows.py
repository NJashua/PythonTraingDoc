# app/routes/follows.py
from flask import Blueprint, request, jsonify
from app.services.follow_service import FollowService

follows_bp = Blueprint('follows', __name__)

follow_service = FollowService()

@follows_bp.route('/follows', methods=['POST'])
def create_follow():
    data = request.get_json()
    follow = follow_service.follow(data['follower_id'], data['following_id'])
    return jsonify(follow.to_dict()), 201

@follows_bp.route('/follows/<follower_id>/<following_id>', methods=['GET'])
def get_follow(follower_id, following_id):
    follow = follow_service.is_following(follower_id, following_id)
    if follow:
        return jsonify(follow.to_dict())
    return jsonify({'error': 'Follow not found'}), 404

@follows_bp.route('/follows/<follower_id>/<following_id>', methods=['DELETE'])
def delete_follow(follower_id, following_id):
    if follow_service.unfollow(follower_id, following_id):
        return jsonify({'message': 'Follow deleted'})
    return jsonify({'error': 'Follow not found'}), 404

@follows_bp.route('/users/<user_id>/followers', methods=['GET'])
def get_user_followers(user_id):
    followers = follow_service.get_followers(user_id)
    return jsonify([follower.to_dict() for follower in followers])

@follows_bp.route('/users/<user_id>/following', methods=['GET'])
def get_user_following(user_id):
    following = follow_service.get_following(user_id)
    return jsonify([follow.to_dict() for follow in following])