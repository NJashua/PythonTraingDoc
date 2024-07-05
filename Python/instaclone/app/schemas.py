from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    content: str

class CommentCreate(BaseModel):
    content: str