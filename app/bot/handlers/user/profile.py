import keyboards as kb

from aiogram import F, Router
from aiogram.types import Message
from middlewares import TestMiddleware

router = Router()


@router.message(F.text == "Редактировать профиль")
async def cmd_start(message: Message):
    await message.reply("Пока в разработке...", reply_markup=kb.user)
