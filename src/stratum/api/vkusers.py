from typing import List

from fastapi import (
    APIRouter,
    Depends,
)

from ..models import *
from ..services.auth import get_current_user
from ..services import VKUsersService


router = APIRouter(
    prefix='/vkusers',
    tags=['vkusers'],
)


@router.get('/{user_id}', response_model=VKUser)
def get_vkuser(
    user_id: int,
    user: User = Depends(get_current_user),
    vkusers_service: VKUsersService = Depends(),
):
    return vkusers_service.get(user_id)


@router.get('/', response_model=List[VKUser])
def get_vkusers(
    user: User = Depends(get_current_user),
    vkusers_service: VKUsersService = Depends(),
):
    return vkusers_service.get_list()


@router.get('/relation', response_model=list[BaseFollowing])
def get_relation(
    user_id_first: int,
    user_id_second: int,
    user: User = Depends(get_current_user),
    vkusers_service: VKUsersService = Depends(),
):
    """Возвращает путь от первого пользователя ко второму по подпискам."""
    return vkusers_service.get_relation(user_id_first, user_id_second)



