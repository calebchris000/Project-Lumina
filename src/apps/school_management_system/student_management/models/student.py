

from src.apps.shared.generate_random_8 import generate_random_8
from src.database.model import User
from tortoise import fields
from src.apps.shared.generate_random_8 import generate_random_8

class Student(User):
    enrolled_class = fields.UUIDField(index=True)
    student_id = fields.IntField(unique=True)
