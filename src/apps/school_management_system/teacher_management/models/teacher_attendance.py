


from src.database.model import BaseModel
from tortoise import fields

class TeacherAttendance(BaseModel):
    teacher = fields.ForeignKeyField('models.Teacher', to_field='teacher_id', related_name='attendances')
    subject = fields.ForeignKeyField('models.Subject', related_name='present_subjects')
    present = fields.BooleanField(null=False)
    reason = fields.TextField(null=True)
    
    class Meta:
        table = 'teacher_attendance'