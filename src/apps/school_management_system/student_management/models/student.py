

from src.apps.shared.generate_user_id import generate_user_id
from src.database.model import User
from tortoise import fields

class Student(User):
    parent_id = fields.UUIDField(null=False)
    enrolled_class = fields.UUIDField(index=True)
    school_contact = fields.ForeignKeyField('models.SchoolContact', related_name='school contact', null=True)
    user_contact = fields.ManyToManyField('models.UserContact', related_name='user contacts', null=True)
    attendance_records = fields.CharField(max_length=20, default=1)
    teacher_id = fields.ForeignKeyField('models.Teacher', related_name='teacher_id', null=True)
