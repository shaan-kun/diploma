from fastapi import (
    APIRouter,
    Depends,
)

from ..models import *
from ..services.auth import get_current_user
from ..services import OrderService


router = APIRouter(
    prefix='/orders',
    tags=['orders'],
)


@router.get('/{order_id}', response_model=Order)
def get_order(
    order_id: int,
    user: User = Depends(get_current_user),
    order_service: OrderService = Depends(),
):
    return order_service.get(order_id)


@router.get('/', response_model=list[Order])
def get_orders(
    user: User = Depends(get_current_user),
    order_service: OrderService = Depends(),
):
    return order_service.get_list()
