# app/routes/comments.py
from flask import Blueprint, request, jsonify
from app.services.comment_service import CommentService

comments_bp = Blueprint('comments', __name__)

comment_service = CommentService()

@comments_bp.route('/comments', methods=['POST'])
def create_comment():
    data = request.get_json()
    comment = comment_service.create_comment(data['post_id'], data['user_id'], data['text'])
    return jsonify(comment.to_dict()), 201

@comments_bp.route('/comments/<comment_id>', methods=['GET'])
def get_comment(comment_id):
    comment = comment_service.get_comment(comment_id)
    if comment:
        return jsonify(comment.to_dict())
    return jsonify({'error': 'Comment not found'}), 404

@comments_bp.route('/comments/<comment_id>', methods=['PUT'])
def update_comment(comment_id):
    data = request.get_json()
    comment = comment_service.update_comment(comment_id, data['text'])
    if comment:
        return jsonify(comment.to_dict())
    return jsonify({'error': 'Comment not found'}), 404

@comments_bp.route('/comments/<comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    if comment_service.delete_comment(comment_id):
        return jsonify({'message': 'Comment deleted'})
    return jsonify({'error': 'Comment not found'}), 404

@comments_bp.route('/posts/<post_id>/comments', methods=['GET'])
def get_post_comments(post_id):
    comments = comment_service.get_comments(post_id)
    return jsonify([comment.to_dict() for comment in comments])