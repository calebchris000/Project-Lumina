


from datetime import date, datetime
from src.database.model import BaseModel
from tortoise import fields

class SchoolAttendance(BaseModel):
    student = fields.ForeignKeyField('models.Student', to_field='student_id', related_name='student_attendances', null=True)
    teacher = fields.ForeignKeyField('models.Teacher', to_field='teacher_id', related_name='teacher_attendances', null=True)
    present = fields.BooleanField(default=False)
    date_of_presence = fields.DateField(default=date.today())
    time_clocked_in = fields.TimeField(null=True)
    reason = fields.TextField(null=True)
    
    class Meta:
        table = 'school_attendances'