from pydantic import BaseModel


class BaseSourceType(BaseModel):
    name: str


class SourceType(BaseSourceType):
    sourcetype_id: int

    class Config:
        orm_mode = True
