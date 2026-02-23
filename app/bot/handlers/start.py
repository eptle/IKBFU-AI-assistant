import keyboards as kb

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from middlewares import TestMiddleware


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f"Привет, я нейроаболтус, который поможет тебе сориентироваться в дебрях БФУ им. И. Канта. Я умею:\n" +
                        f"- Перенапрявлять тебя к наставникам\n" +
                        f"- Перенаправлять тебя в МФЦ\n" +
                        f"- Периодически давать полезную информацию", reply_markup=kb.lets_start)