from pydantic import BaseModel


class SubjectIn(BaseModel):
    name: str
    course_id: ints
    description: str
