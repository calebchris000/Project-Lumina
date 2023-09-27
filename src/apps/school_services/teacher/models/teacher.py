


from database.model import User
from tortoise import fields

class Teacher(User):
    username = fields.CharField(max_length=16)
    subject_taught = fields.ManyToManyField()
    qualifications = fields.ForeignKeyField()
    contact = fields.OneToOneField()
    years_of_experience = fields.DecimalField(max_digits=2)
    supervisor = fields.ForeignKeyField()
    attendance_records = fields.CharField()
    teaching_schedule = fields.ForeignKeyField()