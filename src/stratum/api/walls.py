from fastapi import (
    APIRouter,
    Depends,
)

from ..models import *
from ..services.auth import get_current_user
from ..services import WallService


router = APIRouter(
    prefix='/walls',
    tags=['walls'],
)


@router.get('/{wall_id}', response_model=Wall)
def get_wall(
    wall_id: int,
    user: User = Depends(get_current_user),
    wall_service: WallService = Depends(),
):
    return wall_service.get(wall_id)


@router.get('/', response_model=list[Wall])
def get_walls(
    user: User = Depends(get_current_user),
    walls_service: WallService = Depends(),
):
    return walls_service.get_list()
