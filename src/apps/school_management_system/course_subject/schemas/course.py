from uuid import UUID
from pydantic import BaseModel


class CourseIn(BaseModel):
    name: str = 'Mathematics'
    class_id: UUID = None
    description: str = 'A useful course'
