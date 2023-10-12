



from src.database.model import BaseModel
from tortoise import fields

class UserContact(BaseModel):
    home = fields.IntField(null=False, index=True)
    office = fields.IntField(null=True)
    email_address = fields.CharField(max_length=30, null=True)
    student = fields.ForeignKeyField('models.Student', to_field='student_id', related_name='usercontact', null=True)
    teacher = fields.ForeignKeyField('models.Teacher', to_field='teacher_id', related_name='teacher', null=True)
    
    class Meta:
        table = 'user_contacts'