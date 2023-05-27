from fastapi import (
    APIRouter,
    Depends,
)

from ..models import *
from ..services.auth import get_current_user
from ..services import ClientService


router = APIRouter(
    prefix='/clients',
    tags=['clients'],
)


@router.get('/{client_id}', response_model=Client)
def get_client(
    client_id: int,
    user: User = Depends(get_current_user),
    client_service: ClientService = Depends(),
):
    return client_service.get(client_id)


@router.get('/', response_model=list[Client])
def get_clients(
    user: User = Depends(get_current_user),
    clients_service: ClientService = Depends(),
):
    return clients_service.get_list()
