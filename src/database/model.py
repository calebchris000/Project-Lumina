from datetime import datetime
from uuid import uuid4
from tortoise import fields
from tortoise.models import Model

from src.database.enums import GENDERS, ROLES


class BaseModel(Model):
    id = fields.UUIDField(pk=True, unique=True, index=True)
    created_at = fields.DatetimeField(auto_now_add=True, default=datetime.now())
    updated_at = fields.DatetimeField(auto_now=True, default=datetime.now())
    



class User(BaseModel):
    first_name = fields.CharField(null=False, max_length=50)
    last_name = fields.CharField(null=False, max_length=50)
    date_of_birth = fields.DateField(null=False)
    gender = fields.CharEnumField(GENDERS, description='Sex of user')
    profile_image = fields.CharField(max_length=500,null=True)
    home_address = fields.CharField(max_length=100)
    role = fields.CharEnumField(ROLES, default=ROLES.GUEST)