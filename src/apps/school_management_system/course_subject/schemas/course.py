from pydantic import BaseModel


class CourseIn(BaseModel):
    name: str = 'Mathematics'
    description: str = 'The best subject'
