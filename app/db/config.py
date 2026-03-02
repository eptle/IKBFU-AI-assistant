from pydantic_settings import BaseSettings
from config import Config

class Settings(BaseSettings):
    DATABASE_URL: str = Config.DATABASE_URL

settings = Settings()