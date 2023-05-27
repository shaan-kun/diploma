from typing import List

from fastapi import (
    APIRouter,
    Depends,
    Response,
    status,
)

from ..models import *
from ..models.operations import (
    Operation,
    OperationCreate,
    OperationUpdate
)
from ..services.auth import get_current_user
from ..services.operations import OperationsService


router = APIRouter(
    prefix='/operations',
    tags=['operations'],
)


@router.get(
    '/',
    response_model=List[Operation],
)
def get_operations(
    user: User = Depends(get_current_user),
    operations_service: OperationsService = Depends(),
):
    return operations_service.get_many(user.id)


@router.post(
    '/',
    response_model=Operation,
    status_code=status.HTTP_201_CREATED,
)
def create_operation(
    operation_data: OperationCreate,
    user: User = Depends(get_current_user),
    operations_service: OperationsService = Depends(),
):
    return operations_service.create(
        user.id,
        operation_data,
    )


@router.get(
    '/{operation_id}',
    response_model=Operation,
)
def get_operation(
    operation_id: int,
    user: User = Depends(get_current_user),
    operations_service: OperationsService = Depends(),
):
    return operations_service.get(
        user.id,
        operation_id,
    )


@router.put(
    '/{operation_id}',
    response_model=Operation,
)
def update_operation(
    operation_id: int,
    operation_data: OperationUpdate,
    user: User = Depends(get_current_user),
    operations_service: OperationsService = Depends(),
):
    return operations_service.update(
        user.id,
        operation_id,
        operation_data,
    )


@router.delete(
    '/{operation_id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_operation(
    operation_id: int,
    user: User = Depends(get_current_user),
    operations_service: OperationsService = Depends(),
):
    operations_service.delete(
        user.id,
        operation_id,
    )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
