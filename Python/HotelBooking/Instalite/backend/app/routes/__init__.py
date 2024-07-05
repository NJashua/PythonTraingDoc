# backend/app/routes/__init__.py
from fastapi import APIRouter
from . import auth, comments, follows, likes, notifications, posts

router = APIRouter()

router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(comments.router, prefix="/comments", tags=["comments"])
router.include_router(follows.router, prefix="/follows", tags=["follows"])
router.include_router(likes.router, prefix="/likes", tags=["likes"])
router.include_router(notifications.router, prefix="/notifications", tags=["notifications"])
router.include_router(posts.router, prefix="/posts", tags=["posts"])
