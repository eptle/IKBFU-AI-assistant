# ВЫКЛЮЧИ БЛЯТЬ ВПН ПЕРЕД ЗАПУСКОМ ИЛИ ТЫ ВСЕ НАХУЙ СЛОМАЕШЬ

from config import Config
from telethon import TelegramClient
from datetime import datetime, timedelta
import json

API_ID = int(Config.API_ID)
API_HASH = Config.API_HASH
client = TelegramClient('anon', API_ID, API_HASH)

async def main():
    messages = await client.get_messages("bfunews", limit=10)
    print(*messages, sep='\n\n')



if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())