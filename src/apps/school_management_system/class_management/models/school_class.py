


from src.database.model import BaseModel
from tortoise import fields

class SchoolClass(BaseModel):
    name = fields.CharField(max_length=30)
    size = fields.IntField(max_length=3)
    identifier = fields.CharField(max_length=6, null=True, description="The code name for the class. Eg., A-110")
    description = fields.TextField(null=True)
    student = fields.ManyToManyField('models.Student', related_name='')
    
    class Meta:
        table = 'school_classes'