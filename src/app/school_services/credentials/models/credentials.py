



from src.database.model import BaseModel, User
from tortoise import fields

class Credential(BaseModel):
    username = fields.CharField(max_length=16, null=False)
    password = fields.CharField(max_length=50)
    user = fields.ForeignKeyField('models.Credential', related_name='credential')