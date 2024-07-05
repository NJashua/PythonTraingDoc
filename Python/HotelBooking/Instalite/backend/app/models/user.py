# app/models/user.py
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    profile_picture = db.Column(db.String(128), nullable=True)
    bio = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"