from pydantic import BaseModel


class CourseIn(BaseModel):
    name: str
    category: str
    description: str


class CourseOut(CourseIn):
    
    class Config:
        extra_attributes = True