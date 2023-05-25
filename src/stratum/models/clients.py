from enum import Enum
from pydantic import BaseModel


class ClientType(str, Enum):
    INDIVIDUAL = "физическое лицо"
    LEGAL = "юридическое лицо"


class BaseClient(BaseModel):
    name: str
    type: ClientType
    company_id: int
    user_id: int
    region: str
    address: str


class Client(BaseClient):
    client_id: int

    class Config:
        orm_mode = True
