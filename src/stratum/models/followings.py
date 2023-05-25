from pydantic import BaseModel


class BaseFollowing(BaseModel):
    source_from: int
    source_to: int


class Following(BaseFollowing):
    following_id: int

    class Config:
        orm_mode = True
