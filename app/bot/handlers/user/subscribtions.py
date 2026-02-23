import keyboards as kb

from aiogram import F, Router
from aiogram.types import Message

router = Router()


@router.message(F.text == "Настроить подписки")
async def cmd_start(message: Message):
    await message.reply("Пока в разработке...", reply_markup=kb.user)
