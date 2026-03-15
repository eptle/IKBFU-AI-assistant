from app.bot import keyboards as kb
from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from app.bot.middlewares import TestMiddleware

from app.bot.api_client import start_user


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    payload = {
        "telegram_id": message.from_user.id,
        "username": message.from_user.username,
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
    }

    data = await start_user(payload)

    if data["created"]:
        text = f"Опа, новенький. С подключением \n\n"
    else:
        text = f"Давно не виделись, кожаный \n\n"

    await message.reply(text + f"Привет, я нейроаболтус, который поможет тебе сориентироваться в дебрях БФУ им. И. Канта. Я умею:\n" +
                        f"- Перенапрявлять тебя к наставникам\n" +
                        f"- Перенаправлять тебя в МФЦ\n" +
                        f"- Периодически давать полезную информацию", reply_markup=kb.lets_start)