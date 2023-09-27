from src.database.setup import register_ab
from tortoise import Tortoise

async def start_db(app):
    await register_ab(app)


async def on_shutdown():
    if await Tortoise.close_connections():
        return {"message": "Connection closed successfully"}