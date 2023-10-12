from uuid import UUID
from pydantic import BaseModel


class SchoolClassIn(BaseModel):
    name: str = 'Biology'
    size: int = 10
    identifier: str = 'A-1'
    teacher_id: str = None
    description: str = None