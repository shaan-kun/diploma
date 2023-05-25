from pydantic import BaseModel


class BaseCompany(BaseModel):
    name: str
    city: str
    region: str
    address: str
    contacts: str


class Company(BaseCompany):
    company_id: int

    class Config:
        orm_mode = True
