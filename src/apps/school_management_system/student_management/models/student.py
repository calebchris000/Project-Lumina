

from src.apps.shared.generate_user_id import generate_user_id
from src.database.model import User
from tortoise import fields
from src.apps.shared.generate_user_id import generate_user_id

class Student(User):
    enrolled_class = fields.UUIDField(index=True)
    student_id = fields.IntField(unique=True)
