
from src.database.model import BaseModel
from tortoise import fields

class StudentAttendance(BaseModel):
    student = fields.ForeignKeyField('models.Student', to_field='student_id', related_name='student_classes')
    subject = fields.ForeignKeyField('models.Subject', related_name='subject_attendances')
    present = fields.BooleanField(default=False)
    reason = fields.TextField(null=True)
    
    class Meta:
        table = 'student_attendances'