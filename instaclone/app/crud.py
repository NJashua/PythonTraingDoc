from sqlalchemy.orm import Session
from.models import User, Post, Like, Comment, Follow
from.schemas import PostCreate, CommentCreate

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Post).offset(skip).limit(limit).all()

def create_post(db: Session, post: PostCreate, user_id: int):
    db_post = Post(**post.dict(), user_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def create_like(db: Session, post_id: int, user_id: int):
    db_like = Like(post_id=post_id, user_id=user_id)
    db.add(db_like)
    db.commit()
    db.refresh(db_like)
    return db_like

def create_comment(db: Session, post_id: int, comment: CommentCreate, user_id: int):
    db_comment = Comment(**comment.dict(), post_id=post_id, user_id=user_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_follows(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(Follow).filter(Follow.user_id == user_id).offset(skip).limit(limit).all()

def create_follow(db: Session, user_id: int, follow_id: int):
    db_follow = Follow(user_id=user_id, follow_id=follow_id)
    db.add(db_follow)
    db.commit()
    db.refresh(db_follow)
    return db_follow