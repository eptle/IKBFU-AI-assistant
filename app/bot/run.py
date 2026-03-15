import asyncio
import logging

from config import Config
from aiogram import Bot, Dispatcher
from app.bot.middlewares import TestMiddleware
from app.bot.handlers import setup_routers


bot = Bot(token=Config.TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(setup_routers())
    dp.update.middleware(TestMiddleware())
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
