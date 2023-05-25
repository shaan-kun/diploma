from datetime import datetime

from pydantic import BaseModel


class BaseMessage(BaseModel):
    user_id: int
    content: str
    date: datetime
    attachment: bool = False


class Message(BaseMessage):
    message_id: int

    class Config:
        orm_mode = True
