from fastapi import (
    APIRouter,
    Depends,
)

from ..models import *
from ..services.auth import get_current_user
from ..services import GroupService


router = APIRouter(
    prefix='/groups',
    tags=['groups'],
)


@router.get('/{group_id}', response_model=Group)
def get_group(
    group_id: int,
    user: User = Depends(get_current_user),
    group_service: GroupService = Depends(),
):
    return group_service.get(group_id)


@router.get('/', response_model=list[Group])
def get_groups(
    user: User = Depends(get_current_user),
    group_service: GroupService = Depends(),
):
    return group_service.get_list()
