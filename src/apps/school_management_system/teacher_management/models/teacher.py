from src.apps.shared.generate_random_8 import generate_random_8
from src.apps.school_management_system.teacher_management.enums.teacher import QUALIFICATION
from src.database.model import User
from tortoise import fields


class Teacher(User):
    teacher_id = fields.IntField(unique=True)
    subject_taught = fields.CharField(max_length=20,index=True)
    qualifications = fields.CharEnumField(QUALIFICATION, default=QUALIFICATION.CLEAR_BACKGROUND_CHECK, null=False)
    years_of_experience = fields.DecimalField(max_digits=3, decimal_places=1)
    # supervisor = fields.CharField(max_length=20)
    attendance_records = fields.CharField(max_length=20, default=1)