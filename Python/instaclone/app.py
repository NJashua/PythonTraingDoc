from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .app import crud, schemas
from sqlalchemy.orm import Session
from typing import List

from .app import models
from .app.database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    return crud.create_user(db=db, user=user)

@app.get("/users/me/", response_model=schemas.User)
def read_users_me(db: Session = Depends(get_db), current_user: models.User = Depends(oauth2_scheme)):
    return current_user

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return db_user

@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.post("/posts/", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2_scheme)):
    return crud.create_post(db=db, post=post, current_user=current_user)

@app.get("/posts/", response_model=List[schemas.Post])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    posts = crud.get_posts(db, skip=skip, limit=limit)
    return posts

@app.get("/posts/{post_id}", response_model=schemas.Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.get_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found"
        )
    return db_post

@app.post("/posts/{post_id}/like/", response_model=schemas.Like)
def create_like(post_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2_scheme)):
    return crud.create_like(db=db, post_id=post_id, current_user=current_user)

@app.post("/posts/{post_id}/comment/", response_model=schemas.Comment)
def create_comment(post_id: int, comment: schemas.CommentCreate, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2_scheme)):
    return crud.create_comment(db=db, post_id=post_id, comment=comment, current_user=current_user)

@app.get("/posts/{post_id}/comments/", response_model=List[schemas.Comment])
def read_comments(post_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    comments = crud.get_comments(db, post_id=post_id, skip=skip, limit=limit)
    return comments

@app.post("/users/{user_id}/follow/", response_model=schemas.Follow)
def create_follow(user_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2_scheme)):
    return crud.create_follow(db=db, user_id=user_id, current_user=current_user)

@app.get("/users/{user_id}/followers/", response_model=List[schemas.User])
def read_followers(user_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    followers = crud.get_followers(db, user_id=user_id, skip=skip, limit=limit)
    return followers

@app.get("/users/{user_id}/following/", response_model=List[schemas.User])
def read_following(user_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    following = crud.get_following(db, user_id=user_id, skip=skip, limit=limit)
    return following