from pydantic import BaseModel


class CourseIn(BaseModel):
    name: str
    description: str
