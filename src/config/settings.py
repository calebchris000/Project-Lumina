
from os import getenv
from starlette.config import Config



class Settings:
    _config = Config(env_file='.env')
    secret_key:str = _config('SECRET_KEY')
    database_url = _config('POSTGRESQL_URL')
    
    


def get_settings():
    return Settings()


config = get_settings()