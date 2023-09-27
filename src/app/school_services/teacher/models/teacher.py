from src.database.model import User
from tortoise import fields


class Teacher(User):
    subject_taught = fields.CharField(max_length=20)
    qualifications = fields.CharField(max_length=20)
    contact = fields.CharField(max_length=20)
    years_of_experience = fields.DecimalField(max_digits=3, decimal_places=1)
    supervisor = fields.CharField(max_length=20)
    attendance_records = fields.CharField(max_length=20)
    teaching_schedule = fields.CharField(max_length=20)
