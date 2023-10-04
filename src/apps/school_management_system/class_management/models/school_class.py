


from src.database.model import BaseModel
from tortoise import fields

class SchoolClass(BaseModel):
    name = fields.CharField(max_length=30)
    size = fields.IntField(max_length=3)
    identifier = fields.CharField(max_length=6, null=True, description="The code name for the class. Eg., A-110")
    course = fields.ForeignKeyField('models.Subject', related_name='class_course', null=True)
    description = fields.TextField(null=True)
    
    
    class Meta:
        table = 'school_classes'