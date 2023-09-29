

from src.apps.shared.generate_user_id import generate_user_id
from src.database.model import User
from tortoise import fields

class Student(User):
    parent_id = fields.UUIDField(null=False)
    enrolled_class = fields.ForeignKeyField('models.Course', related_name='course')
    school_email = fields.ForeignKeyField('models.SchoolContact', related_name='school_contact')
    user_contact = fields.ManyToManyField('models.UserContact', related_name='contacts')
    attendance_records = fields.CharField(max_length=20, default=1)
    teacher_id = fields.ForeignKeyField('models.Teacher', related_name='teacher_id')
