from fastapi import APIRouter
from core.apps.api.api import api_router

main_api_router = APIRouter()

main_api_router.include_router(api_router, prefix='', tags=["Api"])
