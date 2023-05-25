from datetime import datetime

from pydantic import BaseModel


class BaseOrder(BaseModel):
    client_id: int
    product_id: int
    count: int
    address: str
    date: datetime


class Order(BaseOrder):
    order_id: int

    class Config:
        orm_mode = True
