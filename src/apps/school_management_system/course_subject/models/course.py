

from src.database.model import BaseModel
from tortoise import fields

class Course(BaseModel):
    name = fields.CharField(max_length=30, unique=True)
    description = fields.TextField()
    school_class = fields.ForeignKeyField('models.SchoolClass', related_name='classes', null=True)
    
    class Meta:
        table = 'courses'