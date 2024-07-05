# app/services/comment_service.py
from app.models import Comment

class CommentService:
    def create_comment(self, post_id, user_id, text):
        comment = Comment(post_id=post_id, user_id=user_id, text=text)
        db.session.add(comment)
        db.session.commit()
        return comment

    def get_comment(self, comment_id):
        return Comment.query.get(comment_id)

    def update_comment(self, comment_id, text):
        comment = Comment.query.get(comment_id)
        if comment:
            comment.text = text
            db.session.commit()
            return comment
        return None

    def delete_comment(self, comment_id):
        comment = Comment.query.get(comment_id)
        if comment:
            db.session.delete(comment)
            db.session.commit()
            return True
        return False

    def get_comments(self, post_id):
        return Comment.query.filter_by(post_id=post_id).all()