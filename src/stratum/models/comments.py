from datetime import datetime

from pydantic import BaseModel


class BaseComment(BaseModel):
    source_id: int
    wall_id: int
    content: str
    date: datetime
    likes: int
    replies: int


class Comment(BaseComment):
    comment_id: int

    class Config:
        orm_mode = True
