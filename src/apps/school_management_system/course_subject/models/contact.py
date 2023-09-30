

from src.database.model import BaseModel
from tortoise import fields

class Contact(BaseModel):
    email = fields.CharField(max_length=30, null=True)
    phone_number = fields.CharField(max_length=12)