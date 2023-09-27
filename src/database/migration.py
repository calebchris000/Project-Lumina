from src.config.settings import config

TORTOISE_ORM = {
    "connections": {"default": config.database_url},
    "apps": {
        "models": {
            "models": ["src.core.models.base", "aerich.models"],
            # "default_connection": "default",
        },
    },
}
