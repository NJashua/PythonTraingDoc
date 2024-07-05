# app/services/like_service.py
from app.models import Like

class LikeService:
    def get_likes(self, post_id):
        return Like.query.filter_by(post_id=post_id).all()

    def get_like(self, like_id):
        return Like.query.get(like_id)

    def create_like(self, post_id, user_id):
        like = Like(post_id=post_id, user_id=user_id)
        db.session.add(like)
        db.session.commit()
        return like

    def delete_like(self, like_id):
        like = Like.query.get(like_id)
        if like:
            db.session.delete(like)
            db.session.commit()
            return True
        return False