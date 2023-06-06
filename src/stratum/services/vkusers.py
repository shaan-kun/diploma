from collections import deque

from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

import stratum.models.vkusers as models
import stratum.tables.vk as tables
from ..database import get_session

from stratum.services.followings import FollowingService


class SourceList(list):
    """Класс для хранения таблицы путей.

    Каждый элемент это список из 3 объектов:
    1) Following.source_from
    2) Following.source_to
    3) список экземпляров Following (путь)
    """
    def get_way(self, source_from: int, source_to: int):
        for row in self:
            if row[0] == source_from and row[1] == source_to:
                return row[2]

    def update_way(self, source_from: int, source_to: int, following: tables.Following):
        for row in self:
            if row[0] == source_from and row[1] == source_to:
                row[2] += [following]
                break


class VKUsersService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, id: int) -> tables.VKUser:
        user = (
            self.session
            .query(tables.VKUser)
            .filter(tables.VKUser.id == id)
            .first()
        )

        if not user:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        return user

    def get(self, id: int) -> tables.VKUser:
        return self._get(id)

    def _get_user_following(self, id: int) -> list[tables.Following]:
        followings = (
            self.session
            .query(tables.Following)
            .filter(tables.Following.source_from == id)
            .all()
        )

        if not followings:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        return followings

    def get_relation(
            self,
            user_id_first: int,
            user_id_second: int
    ) -> list[tables.Following]:
        queue = deque()

        ways = SourceList()
        for f in self._get_user_following(user_id_first):
            queue.append(f)

        while queue:
            following = queue.popleft()

            if not ways.get_way(following.source_from, following.source_to):
                ways += [following.source_from, following.source_to, []]

            ways.update_way(following.source_from, following.source_to, following)

            if following.source_to == user_id_second:
                return ways.get_way(user_id_first, user_id_second)

            for f in self._get_user_following(following.source_to):
                queue.append(f)

        return []

    def get_user
