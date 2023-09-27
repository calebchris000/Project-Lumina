



from database.model import BaseModel
from tortoise import fields

class Credential(BaseModel):
    username = fields.CharField(max_length=16, null=False)
    password = fields.CharField(max_length=50)