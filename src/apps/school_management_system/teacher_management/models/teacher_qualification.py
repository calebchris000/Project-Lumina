


from src.database.model import BaseModel
from tortoise import fields

class TeacherQualification(BaseModel):
    teacher = fields.ForeignKeyField('models.Teacher', to_field='teacher_id', related_name='teacher_qualifications')
    title = fields.CharField(max_length=100)
    institution = fields.CharField(max_length=50)
    year_completed = fields.DateField(null=True)