

from src.database.model import User
from tortoise import fields

class Student(User):
    parent_id = fields.UUIDField(null=False)
    enrolled_class = fields.UUIDField()
    school_email = fields.CharField(max_length=30,null=True)
    contact = fields.ManyToManyField('models.Contact', related_name='contacts')
    