from uuid import UUID
from pydantic import BaseModel


class SubjectIn(BaseModel):
    name: str
    course_id: UUID
    description: str = 'A subset of the given course'
