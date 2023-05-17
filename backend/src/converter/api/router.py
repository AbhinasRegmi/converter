from fastapi import APIRouter

from converter.api.handlers.upload_handler import router as upload_router

router_v1 = APIRouter(prefix="/api/v1")

router_v1.include_router(router=upload_router, tags=["Uploads"])