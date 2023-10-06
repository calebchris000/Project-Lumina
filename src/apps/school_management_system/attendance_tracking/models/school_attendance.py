


from datetime import datetime
from src.database.model import BaseModel
from tortoise import fields

class SchoolAttendance(BaseModel):
    student = fields.ManyToManyField('models.Student', related_name='student_attendances')
    teacher = fields.ManyToManyField('models.Teacher', related_name='teacher_attendances')
    present = fields.BooleanField(default=False)
    date_of_presence = fields.DatetimeField(default=datetime.now())
    reason = fields.TextField(null=True)
    
    class Meta:
        table = 'school_attendances'