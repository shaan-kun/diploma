from decimal import Decimal
from pydantic import BaseModel


class BaseProduct(BaseModel):
    name: str
    shname: str
    price: Decimal
    about: str


class Product(BaseProduct):
    product_id: int

    class Config:
        orm_mode = True
