# app/routes/likes.py
from flask import Blueprint, request, jsonify
from app.services.like_service import LikeService

likes_bp = Blueprint('likes', __name__)

like_service = LikeService()

@likes_bp.route('/likes', methods=['POST'])
def create_like():
    data = request.get_json()
    like = like_service.create_like(data['post_id'], data['user_id'])
    return jsonify(like.to_dict()), 201

@likes_bp.route('/likes/<like_id>', methods=['GET'])
def get_like(like_id):
    like = like_service.get_like(like_id)
    if like:
        return jsonify(like.to_dict())
    return jsonify({'error': 'Like not found'}), 404

@likes_bp.route('/likes/<like_id>', methods=['DELETE'])
def delete_like(like_id):
    if like_service.delete_like(like_id):
        return jsonify({'message': 'Like deleted'})
    return jsonify({'error': 'Like not found'}), 404

@likes_bp.route('/posts/<post_id>/likes', methods=['GET'])
def get_post_likes(post_id):
    likes = like_service.get_likes(post_id)
    return jsonify([like.to_dict() for like in likes])