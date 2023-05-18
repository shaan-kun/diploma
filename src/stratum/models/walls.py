from datetime import date

from pydantic import BaseModel


class BaseWall(BaseModel):
    id: int
    user_id: int
    content: str | None
    date: date
    likes: int
    shared: int
    views: int
    comments: int


class Wall(BaseWall):
    wall_id: int

    class Config:
        orm_mode = True


class WallCreate(BaseWall):
    pass


class WallUpdate(BaseWall):
    pass
