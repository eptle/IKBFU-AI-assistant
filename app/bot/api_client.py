# import httpx
# 
# from config import Config
# 
# 
# API_URL = Config.API_URL
# 
# 
# async def start_user(payload: dict):
# 
#     async with httpx.AsyncClient() as client:
#         response = await client.post(
#             f"{API_URL}/users/start",
#             json=payload
#         )
# 
#     return response.json()


import httpx
import logging
from config import Config

API_URL = Config.API_URL

async def start_user(payload: dict):
    logging.info(f"API_URL value: {API_URL}")
    logging.info(f"Full URL being called: {API_URL}/users/start")
    logging.info(f"Payload: {payload}")
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f"{API_URL}/users/start",
                json=payload
            )
            logging.info(f"Response status: {response.status_code}")
            logging.info(f"Response body: {response.text}")
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logging.error(f"Error in start_user: {type(e).__name__}: {e}")
            raise