

from src.database.model import BaseModel
from tortoise import fields

class Subject(BaseModel):
    name = fields.CharField(max_length=30, unique=True)
    teacher = fields.ForeignKeyField('models.Teacher', related_name='teacher_subjects', null=True)
    from_date = fields.DatetimeField(null=True)
    to_date = fields.DatetimeField(null=True)
    description = fields.TextField(null=True)
    
    class Meta:
        table = 'subjects'