from database.model import BaseModel
from tortoise import fields


class StudentGrade(BaseModel):
    student_id = fields.ForeignKeyField("models.Student", to_field="student_id")
    subject_id = fields.ForeignKeyField('models.Subject', related_name='subject')
    grade = fields.DecimalField(max_digits=4, decimal_places=2)
