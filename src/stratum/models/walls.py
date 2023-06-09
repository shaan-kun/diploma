from datetime import datetime

from pydantic import BaseModel


class BaseWall(BaseModel):
    id: int
    source_id: int
    content: str | None
    date: datetime
    likes: int
    shared: int
    views: int
    comments: int


class Wall(BaseWall):
    wall_id: int

    class Config:
        orm_mode = True
