from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    API_ID = os.getenv("API_ID")
    API_HASH = os.getenv("API_HASH")
    TOKEN = os.getenv("TOKEN")
    ADMINS = os.getenv("ADMINS").split(",")
    CHAT_WHITELIST = os.getenv("CHAT_WHITELIST").split(",")
    ACCESS_KEY = os.getenv("ACCESS_KEY")
    DATABASE_URL = f"postgresql+asyncpg://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@postgres:{os.getenv("POSTGRES_PORT")}/{os.getenv("POSTGRES_DB")}"