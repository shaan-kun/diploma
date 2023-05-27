from fastapi import (
    APIRouter,
    Depends,
)

from ..models import *
from ..services.auth import get_current_user
from ..services import FollowingService


router = APIRouter(
    prefix='/followings',
    tags=['followings'],
)


@router.get('/{following_id}', response_model=Following)
def get_following(
    following_id: int,
    user: User = Depends(get_current_user),
    following_service: FollowingService = Depends(),
):
    return following_service.get(following_id)


@router.get('/', response_model=list[Following])
def get_following(
    user: User = Depends(get_current_user),
    following_service: FollowingService = Depends(),
):
    return following_service.get_list()
