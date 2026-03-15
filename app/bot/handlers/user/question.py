import app.bot.keyboards as kb

from aiogram import F, Router
from aiogram.types import Message

router = Router()


@router.message(F.text == "Задать вопрос")
async def cmd_start(message: Message):
    await message.reply("Введи свой вопрос:", reply_markup=kb.user)
