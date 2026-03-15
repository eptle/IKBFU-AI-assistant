from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas import StartRequest, StartResponse
from app.api.dependencies import get_db
from app.api.services import UsersService


router = APIRouter()


@router.post("/start", response_model=StartResponse)
async def start(
    request: StartRequest,
    db: AsyncSession = Depends(get_db)
):
    service = UsersService(db)
    user, created = await service.register_user(request)

    return StartResponse(
        id=user.id,
        telegram_id=user.telegram_id,
        status=None,
        is_admin=user.is_admin,
        created=created
    )