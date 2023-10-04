


from src.database.model import BaseModel
from tortoise import fields

class TeacherAttendance(BaseModel):
    teacher = fields.ForeignKeyField('models.Teacher', to_field='teacher_id', related_name='attendances')
    present = fields.BooleanField(null=False)
    reason = fields.TextField(null=True)