from datetime import datetime
from uuid import uuid4
from tortoise import fields
from tortoise.models import Model

from src.database.enums import GENDERS, ROLES


class BaseModel(Model):
    id = fields.UUIDField(pk=True, default=uuid4())
    created_at = fields.DatetimeField(auto_now_add=True, default=datetime.now())
    updated_at = fields.DatetimeField(auto_now=True, default=datetime.now())
    



class User(BaseModel):
    first_name = fields.CharField(null=False, max_length=50)
    middle_name = fields.CharField(null=True, max_length=50)
    last_name = fields.CharField(null=False, max_length=50)
    date_of_birth = fields.DatetimeField(null=False)
    email = fields.CharField(max_length=30,null=True)
    gender = fields.CharEnumField(GENDERS, description='Sex of user')
    date_of_enrollment = fields.DateField(null=True)
    profile_image = fields.CharField(max_length=120,null=True)
    roles = fields.CharEnumField(ROLES, default=ROLES.GUEST)