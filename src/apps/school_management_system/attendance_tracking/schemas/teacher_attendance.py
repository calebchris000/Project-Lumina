

from datetime import date, time
from pydantic import BaseModel


class TeacherSchoolAttendanceIn(BaseModel):
    teacher_id: str
    present: bool = True
    date_of_presence: date = date.today()
    time_clocked_in: time = '00:00:00'
    reason: str = None