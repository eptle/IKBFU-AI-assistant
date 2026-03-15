from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.models.users import Users


class UsersService:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def register_user(self, data):

        result = await self.db.execute(
            select(Users).where(Users.telegram_id == data.telegram_id)
        )

        user = result.scalar_one_or_none()

        if user:
            user.username = data.username
            user.first_name = data.first_name
            user.last_name = data.last_name

            created = False

        else:
            user = Users(
                telegram_id=data.telegram_id,
                username=data.username,
                first_name=data.first_name,
                last_name=data.last_name,
            )

            self.db.add(user)
            created = True

        await self.db.commit()
        await self.db.refresh(user)

        return user, created