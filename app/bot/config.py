from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    api_id = os.getenv("api_id")
    api_hash = os.getenv("api_hash")
    token = os.getenv("token")
    admins = os.getenv("admins").split(",")
    pg_link = os.getenv("pg_link")
    chat_whitelist = os.getenv("chat_whitelist").split(",")
    access_key = os.getenv("access_key")