import json
import os
import jwt
from src.apps.authentication.v1.schemas.signup import SignupIn
import bcrypt
from src.config.settings import config
from src.apps.shared.password_hash import hash_password
class SignupService(object):
    @classmethod
    async def signup_user(data_in: SignupIn):
        secret_key = config.secret_key
        hashed_password = await hash_password(data_in.password)
        payload = {**data_in.model_dump(exclude=['password']), 'key': hashed_password}
        encoded_jwt = jwt.encode(payload=payload, key=secret_key)
        return encoded_jwt