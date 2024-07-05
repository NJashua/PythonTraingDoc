# app/routes/notifications.py
from flask import Blueprint, request, jsonify
from app.services.notification_service import NotificationService

notifications_bp = Blueprint('notifications', __name__)

notification_service = NotificationService()

@notifications_bp.route('/notifications', methods=['GET'])
def get_notifications():
    notifications = notification_service.get_notifications()
    return jsonify([notification.to_dict() for notification in notifications])

@notifications_bp.route('/notifications/<notification_id>', methods=['GET'])
def get_notification(notification_id):
    notification = notification_service.get_notification(notification_id)
    if notification:
        return jsonify(notification.to_dict())
    return jsonify({'error': 'Notification not found'}), 404

@notifications_bp.route('/notifications/<notification_id>', methods=['PUT'])
def mark_as_read(notification_id):
    if notification_service.mark_as_read(notification_id):
        return jsonify({'message': 'Notification marked as read'})
    return jsonify({'error': 'Notification not found'}), 404