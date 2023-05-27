from typing import List

from fastapi import (
    APIRouter,
    Depends,
)

from ..models import *
from ..services.auth import get_current_user
from ..services import VKUsersService


router = APIRouter(
    prefix='/users',
    tags=['users'],
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



