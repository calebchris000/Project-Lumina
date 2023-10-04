
from src.database.model import BaseModel
from tortoise import fields

class StudentAttendance(BaseModel):
    student = fields.ForeignKeyField('models.Student', on_delete='CASCADE', to_field='student_id', related_name='studentattendance')
    shool_class = fields.ForeignKeyField('models.SchoolClass', related_name='student_attendances')
    present = fields.BooleanField(default=False)
    reason = fields.TextField(null=True)