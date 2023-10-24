from src.apps.school_management_system.event.enums.event_status import EventStatus
from src.apps.school_management_system.event.enums.event_type import EventType
from src.database.model import BaseModel
from tortoise import fields

class Event(BaseModel):
    name = fields.CharField(max_length=30)
    description = fields.TextField()
    date = fields.DatetimeField()
    status = fields.CharEnumField(EventStatus, default=EventStatus.UPCOMING)
    type = fields.CharEnumField(EventType)