from fastapi import (
    APIRouter,
    Depends,
)

from ..models import *
from ..services.auth import get_current_user
from ..services import SourceService


router = APIRouter(
    prefix='/sources',
    tags=['sources'],
)


@router.get('/{source_id}', response_model=Source)
def get_source(
    source_id: int,
    user: User = Depends(get_current_user),
    source_service: SourceService = Depends(),
):
    return source_service.get(source_id)


@router.get('/', response_model=list[Source])
def get_sources(
    user: User = Depends(get_current_user),
    sources_service: SourceService = Depends(),
):
    return sources_service.get_list()
