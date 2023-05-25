from pydantic import BaseModel


class BaseSource(BaseModel):
    sourcetype_id: int


class Source(BaseSource):
    source_id: int

    class Config:
        orm_mode = True
