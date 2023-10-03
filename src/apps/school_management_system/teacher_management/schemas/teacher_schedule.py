from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class TeacherScheduleIn(BaseModel):
    teacher_id: Optional[int] = None
    subject_id: Optional[UUID]  = None
    from_date: datetime = '2023-10-03T15:30'
    to_date: datetime = '2023-10-03T16:30'