from datetime import date

from pydantic import BaseModel


class BaseVKUser(BaseModel):
    id: int
    domain: str | None
    first_name: str
    second_name: str
    last_name: str
    country: str
    city: str
    bdate: date
    contacts: str


class VKUser(BaseVKUser):
    user_id: int

    class Config:
        orm_mode = True


class Relation:
    id: int
