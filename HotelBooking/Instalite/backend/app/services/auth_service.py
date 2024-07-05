# app/services/auth_service.py
from app.models.user import User
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

class AuthService:
    def login(self, username, password):
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return True
        return False

    def register(self, username, email, password):
        user = User(username=username, email=email, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        return user

    def logout(self):
        logout_user()