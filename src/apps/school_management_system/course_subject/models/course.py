

from src.database.model import BaseModel
from tortoise import fields

class Course(BaseModel):
    name = fields.CharField(max_length=30, unique=True)
    description = fields.TextField()
    subjects = fields.ManyToManyField('models.Subject', related_name='subjects')
    
    class Meta:
        table = 'courses'