from tortoise import fields

from src.database.model import BaseModel


class Schedule(BaseModel):
    from_date = fields.DatetimeField(null=True)
    to_date = fields.DatetimeField()