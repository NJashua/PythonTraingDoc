# app/routes/posts.py
from flask import Blueprint, request, jsonify
from app.services.post_service import PostService

posts_bp = Blueprint('posts', __name__)

post_service = PostService()

@posts_bp.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    post = post_service.create_post(data['user_id'], data['image'], data['caption'])
    return jsonify(post.to_dict()), 201

@posts_bp.route('/posts/<post_id>', methods=['GET'])
def get_post(post_id):
    post = post_service.get_post(post_id)
    if post:
        return jsonify(post.to_dict())
    return jsonify({'error': 'Post not found'}), 404

@posts_bp.route('/posts/<post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.get_json()
    post = post_service.update_post(post_id, data['image'], data['caption'])
    if post:
        return jsonify(post.to_dict())
    return jsonify({'error': 'Post not found'}), 404

@posts_bp.route('/posts/<post_id>', methods=['DELETE'])
def delete_post(post_id):
    if post_service.delete_post(post_id):
        return jsonify({'message': 'Post deleted'})
    return jsonify({'error': 'Post not found'}), 404