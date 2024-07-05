from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta
from . import crud, models, schemas
from .database import SessionLocal, engine
from .security import authenticate_user, create_access_token, get_current_user
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")

# Create database tables
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Routes
@app.get("/docs", response_class=HTMLResponse)
async def get_docs(request: Request):
    return templates.TemplateResponse("docs.html", {"request": request})

@app.get("/openapi.json", response_class=JSONResponse)
async def get_openapi():
    return {"message": "Hello World"}

@app.post("/token")
async def get_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(current_user: models.User = Depends(get_current_user)):
    return current_user

@app.get("/posts/")
async def read_posts(skip: int = 0, limit: int = 10):
    db = SessionLocal()
    posts = crud.get_posts(db, skip=skip, limit=limit)
    db.close()
    return posts

@app.post("/posts/")
async def create_post(post: schemas.PostCreate, current_user: models.User = Depends(get_current_user)):
    db = SessionLocal()
    post = crud.create_post(db, post, current_user.id)
    db.close()
    return post

@app.get("/posts/{post_id}")
async def read_post(post_id: int):
    db = SessionLocal()
    post = crud.get_post(db, post_id)
    db.close()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.post("/posts/{post_id}/likes/")
async def create_like(post_id: int, current_user: models.User = Depends(get_current_user)):
    db = SessionLocal()
    like = crud.create_like(db, post_id, current_user.id)
    db.close()
    return like

@app.post("/posts/{post_id}/comments/")
async def create_comment(post_id: int, comment: schemas.CommentCreate, current_user: models.User = Depends(get_current_user)):
    db = SessionLocal()
    comment = crud.create_comment(db, post_id, comment, current_user.id)
    db.close()
    return comment

@app.get("/users/{username}")
async def read_user(username: str):
    db = SessionLocal()
    user = crud.get_user_by_username(db, username)
    db.close()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users/{username}/follows/")
async def read_follows(username: str, skip: int = 0, limit: int = 10):
    db = SessionLocal()
    user = crud.get_user_by_username(db, username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    follows = crud.get_follows(db, user.id, skip=skip, limit=limit)
    db.close()
    return follows

@app.post("/users/{username}/follows/")
async def create_follow(username: str, current_user: models.User = Depends(get_current_user)):
    db = SessionLocal()
    user = crud.get_user_by_username(db, username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    follow = crud.create_follow(db, current_user.id, user.id)
    db.close()
    return follow
