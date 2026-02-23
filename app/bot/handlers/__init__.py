from aiogram import Router

from .start import router as start_router
from .registration import router as registration_router
from .admin import router as admin_router
from .user import setup_user_routers


def setup_routers() -> Router:
    router = Router()

    router.include_router(start_router)
    router.include_router(registration_router)
    router.include_router(admin_router)
    router.include_router(setup_user_routers())

    return router