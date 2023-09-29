

from src.apps.shared.generate_user_id import generate_user_id
from src.database.model import User
from tortoise import fields

class Student(User):
    parent_id = fields.UUIDField(null=False)
    enrolled_class = fields.ForeignKeyField('models.Course', related_name='course')
    school_email = fields.CharField(max_length=30,null=True)
    contact = fields.ManyToManyField('models.Contact', related_name='contacts')
    attendance_records = fields.CharField(max_length=20, default=1)
    teacher_id = fields.IntField(default=generate_user_id())
