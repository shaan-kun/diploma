from typing import (
    List,
    Optional,
)

from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from .. import tables
from ..database import get_session


class VKUsersService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_many(self) -> List[tables.VKUser]:
        operations = (
            self.session
            .query(tables.VKUser)
            .order_by(
                tables.VKUser.user_id.desc(),
            )
            .all()
        )
        return operations

    def get(
        self,
        user_id: int,
    ) -> tables.VKUser:
        user = self._get(user_id)
        return user

    def _get(self, user_id: int) -> Optional[tables.VKUser]:
        user = (
            self.session
            .query(tables.VKUser)
            .filter(tables.VKUser.user_id == user_id)
            .first()
        )
        if not user:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return user
