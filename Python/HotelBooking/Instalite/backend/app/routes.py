# app/routes.py
from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from app.services.post_service import PostService
from app.services.comment_service import CommentService
from app.services.like_service import LikeService
from app.services.follow_service import FollowService
from app.services.notification_service import NotificationService

bp = Blueprint('api', __name__)

user_service = UserService()
post_service = PostService()
comment_service = CommentService()
like_service = LikeService()
follow_service = FollowService()
notification_service = NotificationService()

@bp.route('/users', methods=['GET'])
def get_users():
    users = user_service.get_users()
    return jsonify([user.to_dict() for user in users])

@bp.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = user_service.get_user(username)
    if user:
        return jsonify(user.to_dict())
    return jsonify({'error': 'User not found'}), 404

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = user_service.create_user(data['username'], data['email'], data['password'])
    return jsonify(user.to_dict()), 201

@bp.route('/posts', methods=['GET'])
def get_posts():
    posts = post_service.get_posts()
    return jsonify([post.to_dict() for post in posts])

@bp.route('/posts/<post_id>', methods=['GET'])
def get_post(post_id):
    post = post_service.get_post(post_id)
    if post:
        return jsonify(post.to_dict())
    return jsonify({'error': 'Post not found'}), 404

@bp.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    post = post_service.create_post(data['user_id'], data['image'], data['caption'])
    return jsonify(post.to_dict()), 201

@bp.route('/comments', methods=['GET'])
def get_comments():
    comments = comment_service.get_comments()
    return jsonify([comment.to_dict() for comment in comments])

@bp.route('/comments/<comment_id>', methods=['GET'])
def get_comment(comment_id):
    comment = comment_service.get_comment(comment_id)
    if comment:
        return jsonify(comment.to_dict())
    return jsonify({'error': 'Comment not found'}), 404

@bp.route('/comments', methods=['POST'])
def create_comment():
    data = request.get_json()
    comment = comment_service.create_comment(data['post_id'], data['user_id'], data['text'])
    return jsonify(comment.to_dict()), 201

@bp.route('/likes', methods=['GET'])
def get_likes():
    likes = like_service.get_likes()
    return jsonify([like.to_dict() for like in likes])

@bp.route('/likes/<like_id>', methods=['GET'])
def get_like(like_id):
    like = like_service.get_like(like_id)
    if like:
        return jsonify(like.to_dict())
    return jsonify({'error': 'Like not found'}), 404

@bp.route('/likes', methods=['POST'])
def create_like():
    data = request.get_json()
    like = like_service.create_like(data['post_id'], data['user_id'])
    return jsonify(like.to_dict()), 201

@bp.route('/follows', methods=['GET'])
def get_follows():
    follows = follow_service.get_follows()
    return jsonify([follow.to_dict() for follow in follows])

@bp.route('/follows/<follow_id>', methods=['GET'])
def get_follow(follow_id):
    follow = follow_service.get_follow(follow_id)
    if follow:
        return jsonify(follow.to_dict())
    return jsonify({'error': 'Follow not found'}), 404

@bp.route('/follows', methods=['POST'])
def create_follow():
    data = request.get_json()
    follow = follow_service.create_follow(data['follower_id'], data['following_id'])
    return jsonify(follow.to_dict()), 201

@bp.route('/notifications', methods=['GET'])
def get_notifications():
    notifications = notification_service.get_notifications()
    return jsonify([notification.to_dict() for notification in notifications])

@bp.route('/notifications/<notification_id>', methods=['GET'])
def get_notification(notification_id):
    notification = notification_service.get_notification(notification_id)
    if notification:
        return jsonify(notification.to_dict())
    return jsonify({'error': 'Notification not found'}), 404

@bp.route('/notifications', methods=['POST'])
def create_notification():
    data = request.get_json()
    notification = notification_service.create_notification(data['user_id'], data['message'])
    return jsonify(notification.to_dict()), 201