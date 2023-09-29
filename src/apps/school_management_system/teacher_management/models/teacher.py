from apps.shared.generate_user_id import generate_user_id
from src.apps.school_management_system.teacher_management.directives.enums.teacher import QUALIFICATION
from src.database.model import User
from tortoise import fields


class Teacher(User):
    subject_taught = fields.ForeignKeyField('models.Course', related_name='subject')
    qualifications = fields.CharEnumField(QUALIFICATION, default=QUALIFICATION.CLEAR_BACKGROUND_CHECK, null=False)
    contact = fields.ManyToManyField('models.Contact', related_name='contact')
    years_of_experience = fields.DecimalField(max_digits=3, decimal_places=1)
    supervisor = fields.CharField(max_length=20)
    attendance_records = fields.CharField(max_length=20, default=1)
    teaching_schedule = fields.CharField(max_length=20)
    teacher_id = fields.IntField(default=generate_user_id())
