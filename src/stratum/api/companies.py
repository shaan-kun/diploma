from fastapi import (
    APIRouter,
    Depends,
)

from ..models import *
from ..services.auth import get_current_user
from ..services import CompanyService


router = APIRouter(
    prefix='/companies',
    tags=['companies'],
)


@router.get('/{company_id}', response_model=Company)
def get_company(
    company_id: int,
    user: User = Depends(get_current_user),
    company_service: CompanyService = Depends(),
):
    return company_service.get(company_id)


@router.get('/', response_model=list[Company])
def get_companies(
    user: User = Depends(get_current_user),
    company_service: CompanyService = Depends(),
):
    return company_service.get_list()
