# app/services/notification_service.py
from app.models import Notification

class NotificationService:
    def get_notifications(self):
        return Notification.query.all()

    def get_notification(self, notification_id):
        return Notification.query.get(notification_id)

    def create_notification(self, user_id, message):
        notification = Notification(user_id=user_id, message=message)
        db.session.add(notification)
        db.session.commit()
        return notification

    def mark_as_read(self, notification_id):
        notification = Notification.query.get(notification_id)
        if notification:
            notification.read = True
            db.session.commit()
            return True
        return False