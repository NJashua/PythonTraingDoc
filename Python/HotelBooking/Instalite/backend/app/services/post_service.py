# app/services/post_service.py
from app.models import Post

class PostService:
    def get_posts(self):
        return Post.query.all()

    def get_post(self, post_id):
        return Post.query.get(post_id)

    def create_post(self, user_id, image, caption):
        post = Post(user_id=user_id, image=image, caption=caption)
        db.session.add(post)
        db.session.commit()
        return post

    def update_post(self, post_id, image, caption):
        post = Post.query.get(post_id)
        if post:
            post.image = image
            post.caption = caption
            db.session.commit()
            return post
        return None

    def delete_post(self, post_id):
        post = Post.query.get(post_id)
        if post:
            db.session.delete(post)
            db.session.commit()
            return True
        return False