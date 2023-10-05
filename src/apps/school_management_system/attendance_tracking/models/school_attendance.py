


from src.database.model import BaseModel
from tortoise import fields

class SchoolAttendance(BaseModel):
    student = fields.ForeignKeyField('models.Student', related_name='school_attendances', null=True)
    teacher = fields.ForeignKeyField('models.Teacher', related_name='school_attendances', null=True)
    present = fields.BooleanField(default=False)
    reason = fields.TextField(null=True)
    
    class Meta:
        table = 'school_attendances'