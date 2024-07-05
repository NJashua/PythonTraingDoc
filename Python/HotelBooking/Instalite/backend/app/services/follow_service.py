# app/services/follow_service.py
from app.models import Follow

class FollowService:
    def get_followers(self, user_id):
        return Follow.query.filter_by(following_id=user_id).all()

    def get_following(self, user_id):
        return Follow.query.filter_by(follower_id=user_id).all()

    def follow(self, follower_id, following_id):
        follow = Follow(follower_id=follower_id, following_id=following_id)
        db.session.add(follow)
        db.session.commit()
        return follow

    def unfollow(self, follower_id, following_id):
        follow = Follow.query.filter_by(follower_id=follower_id, following_id=following_id).first()
        if follow:
            db.session.delete(follow)
            db.session.commit()
            return True
        return False

    def is_following(self, follower_id, following_id):
        return Follow.query.filter_by(follower_id=follower_id, following_id=following_id).first()