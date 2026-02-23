from aiogram import Router

from .question import router as question_router
from .profile import router as profile_router
from .subscribtions import router as subs_router


def setup_user_routers() -> Router:
    router = Router()

    router.include_router(question_router)
    router.include_router(profile_router)
    router.include_router(subs_router)

    return router