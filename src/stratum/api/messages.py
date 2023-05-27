from fastapi import (
    APIRouter,
    Depends,
)

from ..models import *
from ..services.auth import get_current_user
from ..services import MessageService


router = APIRouter(
    prefix='/messages',
    tags=['messages'],
)


@router.get('/{message_id}', response_model=Message)
def get_message(
    message_id: int,
    user: User = Depends(get_current_user),
    message_service: MessageService = Depends(),
):
    return message_service.get(message_id)


@router.get('/', response_model=list[Message])
def get_messages(
    user: User = Depends(get_current_user),
    message_service: MessageService = Depends(),
):
    return message_service.get_list()
