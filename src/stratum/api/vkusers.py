from typing import List

from fastapi import (
    APIRouter,
    Depends,
)

from .. import models
from ..services.auth import get_current_user
from ..services.vkusers import VKUsersService


router = APIRouter(
    prefix='/users',
    tags=['users'],
)


@router.get('/', response_model=List[models.VKUser])
def get_users(
    user: models.User = Depends(get_current_user),
    vkusers_service: VKUsersService = Depends(),
):
    return vkusers_service.get_many()


@router.get('/{user_id}', response_model=models.VKUser)
def get_user(
    user_id: int,
    user: models.User = Depends(get_current_user),
    vkusers_service: VKUsersService = Depends(),
):
    return vkusers_service.get(user_id)
