# backend/app/models/follow.py
from sqlalchemy import Column, Integer, ForeignKey
from .base import Base

class Follow(Base):
    id = Column(Integer, primary_key=True, index=True)
    follower_id = Column(Integer, ForeignKey('user.id'))
    followed_id = Column(Integer, ForeignKey('user.id'))
