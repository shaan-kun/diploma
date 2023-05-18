from enum import Enum

from pydantic import BaseModel


class VKUserKind(str, Enum):
    USER = 'user'
    GROUP = 'group'
    APPLICATION = 'application'


class BaseVKUser(BaseModel):
    id: int
    domain: str
    name: str
    type: VKUserKind


class VKUser(BaseVKUser):
    user_id: int

    class Config:
        orm_mode = True


class VKUserCreate(BaseVKUser):
    pass


class VKUserUpdate(BaseVKUser):
    pass
