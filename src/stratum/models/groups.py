from pydantic import BaseModel


class BaseGroup(BaseModel):
    id: int
    screen_name: str | None
    name: str
    description: str
    type: str
    country: str
    city: str
    contacts: str


class Group(BaseGroup):
    group_id: int

    class Config:
        orm_mode = True
