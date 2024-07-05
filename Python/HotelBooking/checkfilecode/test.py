from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordBearer, OAuth2
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

class User(BaseModel):
    id: int
    username: str
    email: str
    profile_picture: str

class Post(BaseModel):
    id: int
    user_id: int
    content: str
    image_url: str

class Comment(BaseModel):
    id: int
    post_id: int
    user_id: int
    content: str

class Like(BaseModel):
    id: int
    post_id: int
    user_id: int

class Follow(BaseModel):
    id: int
    user_id: int
    followed_user_id: int

users = [
    User(id=1, username="john", email="john@example.com", profile_picture="https://example.com/john.jpg"),
    User(id=2, username="jane", email="jane@example.com", profile_picture="https://example.com/jane.jpg"),
]

posts = [
    Post(id=1, user_id=1, content="Hello, world!", image_url="https://example.com/post1.jpg"),
    Post(id=2, user_id=2, content="This is a test post", image_url="https://example.com/post2.jpg"),
]

comments = [
    Comment(id=1, post_id=1, user_id=2, content="Nice post!"),
    Comment(id=2, post_id=2, user_id=1, content="Thanks!"),
]

likes = [
    Like(id=1, post_id=1, user_id=2),
    Like(id=2, post_id=2, user_id=1),
]

follows = [
    Follow(id=1, user_id=1, followed_user_id=2),
    Follow(id=2, user_id=2, followed_user_id=1),
]

@app.get("/users/")
async def read_users():
    return users

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/users/")
async def create_user(user: User):
    users.append(user)
    return user

@app.get("/posts/")
async def read_posts():
    return posts

@app.get("/posts/{post_id}")
async def read_post(post_id: int):
    for post in posts:
        if post.id == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")

@app.post("/posts/")
async def create_post(post: Post):
    posts.append(post)
    return post

@app.get("/comments/{post_id}")
async def read_comments(post_id: int):
    comments_for_post = [comment for comment in comments if comment.post_id == post_id]
    return comments_for_post

@app.post("/comments/")
async def create_comment(comment: Comment):
    comments.append(comment)
    return comment

@app.get("/likes/{post_id}")
async def read_likes(post_id: int):
    likes_for_post = [like for like in likes if like.post_id == post_id]
    return likes_for_post

@app.post("/likes/")
async def create_like(like: Like):
    likes.append(like)
    return like

@app.get("/follows/{user_id}")
async def read_follows(user_id: int):
    follows_for_user = [follow for follow in follows if follow.user_id == user_id]
    return follows_for_user

@app.post("/follows/")
async def create_follow(follow: Follow):
    follows.append(follow)
    return follow

@app.get("/activity-feeds/{user_id}")
async def read_activity_feed(user_id: int):
    activity_feed = []
    for post in posts:
        if post.user_id == user_id:
            activity_feed.append(post)
    for comment in comments:
        if comment.user_id == user_id:
            activity_feed.append(comment)
    for like in likes:
        if like.user_id == user_id:
            activity_feed.append(like)
    return activity_feed

@app.get("/notifications/{user_id}")
async def read_notifications(user_id: int):
    notifications = []
    for like in likes:
        if like.post_id in [post.id for post in posts if post.user_id == user_id]:
            notifications.append({"type": "like", "post_id": like.post_id, "user_id": like.user_id})
    for comment in comments:
        if comment.post_id in [post.id for post in posts if post.user_id == user_id]:
            notifications.append({"type": "comment", "post_id": comment.post_id, "user_id": comment.user_id})
    for follow in follows:
        if follow.followed_user_id == user_id:
            notifications.append({"type": "follow", "user_id": follow.user_id})
    return notifications

@app.get("/images/")
async def read_images():
    return [{"id": 1, "url": "https://example.com/image1.jpg"}, {"id": 2, "url": "https://example.com/image2.jpg"}]

@app.post("/images/")
async def create_image(image: UploadFile = Depends()):
    # Save the image to a database or file system
    return {"id": 1, "url": "https://example.com/image1.jpg"}

@app.get("/profile/{user_id}")
async def read_profile(user_id: int):
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/feed/{user_id}")
async def read_feed(user_id: int):
    feed = []
    for post in posts:
        if post.user_id == user_id or post.user_id in [follow.followed_user_id for follow in follows if follow.user_id == user_id]:
            feed.append(post)
    return feed

@app.get("/post/{post_id}")
async def read_post(post_id: int):
    post = next((post for post in posts if post.id == post_id), None)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.post("/post/{post_id}/like")
async def like_post(post_id: int, user_id: int):
    like = Like(post_id=post_id, user_id=user_id)
    likes.append(like)
    return like

@app.post("/post/{post_id}/comment")
async def comment_post(post_id: int, user_id: int, content: str):
    comment = Comment(post_id=post_id, user_id=user_id, content=content)
    comments.append(comment)
    return comment

@app.get("/post/{post_id}/comments")
async def read_comments(post_id: int):
    comments_for_post = [comment for comment in comments if comment.post_id == post_id]
    return comments_for_post

@app.get("/post/{post_id}/likes")
async def read_likes(post_id: int):
    likes_for_post = [like for like in likes if like.post_id == post_id]
    return likes_for_post

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)