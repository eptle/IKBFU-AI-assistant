import asyncio
import logging

from config import Config
from aiogram import Bot, Dispatcher
from middlewares import TestMiddleware
from handlers import setup_routers


bot = Bot(token=Config.token)
dp = Dispatcher()


async def main():
    dp.include_router(setup_routers())
    dp.update.middleware(TestMiddleware())
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
