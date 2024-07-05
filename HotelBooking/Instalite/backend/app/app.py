# app/app.py
from flask import Flask
from app.extensions import db
from app.routes.users import users_bp
from app.routes.posts import posts_bp
from app.routes.comments import comments_bp
from app.routes.likes import likes_bp
from app.routes.follows import follows_bp
from app.routes.notifications import notifications_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)

    app.register_blueprint(users_bp)
    app.register_blueprint(posts_bp)
    app.register_blueprint(comments_bp)
    app.register_blueprint(likes_bp)
    app.register_blueprint(follows_bp)
    app.register_blueprint(notifications_bp)

    return app