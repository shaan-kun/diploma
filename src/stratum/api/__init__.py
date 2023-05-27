from fastapi import APIRouter

from . import (
    operations,
    auth,
    clients,
    comments,
    companies,
    followings,
    groups,
    messages,
    orders,
    products,
    reports,
    sources,
    vkusers,
    walls,
)


router = APIRouter()

# router.include_router(operations.router)
router.include_router(auth.router)
router.include_router(clients.router)
router.include_router(comments.router)
router.include_router(companies.router)
router.include_router(followings.router)
router.include_router(groups.router)
router.include_router(messages.router)
router.include_router(orders.router)
router.include_router(products.router)
router.include_router(reports.router)
router.include_router(sources.router)
router.include_router(vkusers.router)
router.include_router(walls.router)
