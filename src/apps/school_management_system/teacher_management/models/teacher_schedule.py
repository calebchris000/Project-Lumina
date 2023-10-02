



from src.database.model import BaseModel
from tortoise import fields

class TeacherSchedule(BaseModel):
    teacher = fields.ForeignKeyField('models.Teacher', related_name='teacher')
    subject = fields.ForeignKeyField('models.Subject', related_name='subject')
    from_date = fields.TimeField()
    to_date = fields.TimeField()