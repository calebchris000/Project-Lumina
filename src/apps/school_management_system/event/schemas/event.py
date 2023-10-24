from datetime import datetime, timedelta
from pydantic import BaseModel


class EventIn(BaseModel):
    name: str = None
    description: str = None
    date: datetime = datetime.now() + timedelta(days=1)
    status: str = "upcoming"
    type: str = "academic"
