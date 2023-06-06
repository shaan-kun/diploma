from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

import stratum.models.followings as models
import stratum.tables.vk as tables
from ..database import get_session


class FollowingService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, following_id: int) -> tables.Following:
        following = (
            self.session
            .query(tables.VKUser)
            .filter(tables.Following.following_id == following_id)
            .first()
        )

        if not following:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        return following

    def get(self, following_id: int) -> tables.Following:
        return self._get(following_id)

    def get_user_following(self, id: int) -> tables.Following:
        followings = (
            self.session
            .query(tables.Following)
            .filter(tables.Following.source_from == id)
            .all()
        )

        if not followings:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        return followings
