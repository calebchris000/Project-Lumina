


from app.school_services.parent.directives.enums.parent import RELATIONSHIP
from database.model import BaseModel
from tortoise import fields

class Parent(BaseModel):
    first_name = fields.CharField(max_length=50)
    last_name = fields.CharField(max_length=50)
    relationship = fields.CharEnumField(RELATIONSHIP, default=RELATIONSHIP.UNKNOWN)
    contact = fields.ManyToManyField('models.Contact', null=False, related_name='contacts')
    email = fields.CharField(max_length=50)
    home_address = fields.CharField(max_length=100)
    occupation = fields.CharField(max_length=20)
    student_id = fields.ForeignKeyField('models.Student', null=False, related_name='students')