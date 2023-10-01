

from src.database.model import BaseModel
from tortoise import fields

class Course(BaseModel):
    name = fields.CharField(max_length=30, unique=True)
    course_id = fields.IntField(max_length=8, index=True)
    description = fields.TextField()
    