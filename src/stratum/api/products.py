from fastapi import (
    APIRouter,
    Depends,
)

from ..models import *
from ..services.auth import get_current_user
from ..services import ProductService


router = APIRouter(
    prefix='/products',
    tags=['products'],
)


@router.get('/{product_id}', response_model=Product)
def get_product(
    product_id: int,
    user: User = Depends(get_current_user),
    product_service: ProductService = Depends(),
):
    return product_service.get(product_id)


@router.get('/', response_model=list[Product])
def get_products(
    user: User = Depends(get_current_user),
    product_service: ProductService = Depends(),
):
    return product_service.get_list()
