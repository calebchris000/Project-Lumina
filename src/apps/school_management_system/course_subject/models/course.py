

from src.database.model import BaseModel
from tortoise import fields

class Course(BaseModel):
    name = fields.CharField(max_length=30, unique=True)
    description = fields.TextField()
    subjects = fields.ManyToManyField('models.Subject', related_name='subjects')
    classes = fields.ManyToManyField('models.SchoolClass', related_name='classes')
    
    class Meta:
        table = 'courses'