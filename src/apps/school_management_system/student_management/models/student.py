from src.apps.shared.generate_random_8 import generate_random_8
from src.database.model import User
from tortoise import fields
from src.apps.shared.generate_random_8 import generate_random_8

class Student(User):
    # enrolled_class_ids = fields.JSONField()
    grade = fields.CharField(max_length=2)
    student_id = fields.CharField(unique=True, max_length=10, index=True)