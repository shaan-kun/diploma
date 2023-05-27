from fastapi import (
    APIRouter,
    Depends,
)

from ..models import *
from ..services.auth import get_current_user
from ..services import CommentService


router = APIRouter(
    prefix='/comments',
    tags=['comments'],
)


@router.get('/{comment_id}', response_model=Comment)
def get_comment(
    comment_id: int,
    user: User = Depends(get_current_user),
    comment_service: CommentService = Depends(),
):
    return comment_service.get(comment_id)


@router.get('/', response_model=list[Comment])
def get_comments(
    user: User = Depends(get_current_user),
    comments_service: CommentService = Depends(),
):
    return comments_service.get_list()
