

from src.database.model import BaseModel
from tortoise import fields

class Subject(BaseModel):
    name = fields.CharField(max_length=30, unique=True)
    course = fields.ForeignKeyField('models.Course', related_name='course')
    description = fields.TextField()
    