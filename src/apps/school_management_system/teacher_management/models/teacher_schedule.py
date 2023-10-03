



from src.database.model import BaseModel
from tortoise import fields

class TeacherSchedule(BaseModel):
    teacher = fields.ForeignKeyField('models.Teacher', related_name='teachers')
    subject = fields.ForeignKeyField('models.Subject', related_name='subjects')
    from_date = fields.DatetimeField()
    to_date = fields.DatetimeField()