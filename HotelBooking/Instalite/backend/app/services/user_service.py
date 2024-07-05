# app/services/user_service.py
from app.models import User

class UserService:
    def get_users(self):
        return User.query.all()

    def get_user(self, username):
        return User.query.filter_by(username=username).first()

    def create_user(self, username, email, password):
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    def get_posts(self, user_id):
        return Post.query.filter_by(user_id=user_id).all()

    def get_followers(self, user_id):
        return Follow.query.filter_by(following_id=user_id).all()

    def get_following(self, user_id):
        return Follow.query.filter_by(follower_id=user_id).all()