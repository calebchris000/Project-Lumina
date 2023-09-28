from tortoise import fields

from src.database.model import BaseModel


class Course(BaseModel):
    name = fields.CharField(max_length=20)
    category = fields.UUIDField()
    description = fields.TextField()