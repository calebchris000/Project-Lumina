



from database.model import BaseModel
from tortoise import fields

class UserContact(BaseModel):
    user_id = fields.UUIDField(null=False)
    home = fields.IntField(null=False, index=True)
    office = fields.IntField(null=True)
    email_address = fields.CharField(max_length=30, null=True)
