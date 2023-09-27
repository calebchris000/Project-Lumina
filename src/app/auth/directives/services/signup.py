import json
import os
import jwt
from src.app.auth.v1.schemas.signup import SignupIn
import bcrypt
from src.config.settings import config
class SignupService(object):
    @classmethod
    async def signup_User(self, data_in: SignupIn):
        secret_key = config.secret_key
        hashed_password = await self.hash_password(data_in.password)
        payload = {**data_in.model_dump(exclude=['password']), 'key': hashed_password}
        encoded_jwt = jwt.encode(payload=payload, key=secret_key)
        return encoded_jwt
        

    @staticmethod
    async def hash_password(password: str):
        if not password:
            return None
        password_bytes = password.encode("utf-8")
        salt = bcrypt.gensalt(rounds=12)
        hashed_password = bcrypt.hashpw(password=password_bytes, salt=salt)

        return str(hashed_password)
