from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from ..models import *
from ..tables import *
from ..database import get_session


class ProductService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get(self, id: int):
        pass
