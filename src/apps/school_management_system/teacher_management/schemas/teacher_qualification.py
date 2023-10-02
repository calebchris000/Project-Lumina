
from datetime import date
from pydantic import BaseModel


class TeacherQualificationIn(BaseModel):
    title: str = 'Bachelor of Science'
    institution: str = 'Berkley'
    year_completed: date = '2020-05-05'