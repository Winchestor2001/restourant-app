from fastapi import APIRouter

from src.api.v1.routers.category import router as category_router
from src.api.v1.routers.admin import router as admin_router

main_router = APIRouter()

main_router.include_router(category_router)
main_router.include_router(admin_router)
