



from database.model import BaseModel
from tortoise import fields

class SchoolContact(BaseModel):
    user_id = fields.UUIDField(null=False)
    email_address = fields.CharField(max_length=30, null=True)
