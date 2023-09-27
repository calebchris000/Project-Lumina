from tortoise.contrib.fastapi import register_tortoise
from src.config.settings import config
from anyio import sleep


async def register_ab(app):
    while True:
        try:
            register_tortoise(
                app,
                db_url=config.database_url,
                modules={"models": ["src.core.models.base", 'src.database.model']},
                generate_schemas=True,
                add_exception_handlers=True
            )
            break
        except Exception as e:
            sleep(5)
            print("Failed to generate schema", e)
