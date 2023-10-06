
from src.database.model import BaseModel
from tortoise import fields

class StudentAttendance(BaseModel):
    student = fields.ForeignKeyField('models.Student',related_name='student_classes')
    school_class = fields.ForeignKeyField('models.SchoolClass', related_name='student_attendances')
    present = fields.BooleanField(default=False)
    class_date_present = fields.ForeignKeyField('models.Subject', related_name='present_classes')
    reason = fields.TextField(null=True)
    
    class Meta:
        table = 'student_attendances'