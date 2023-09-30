


from datetime import date
from uuid import UUID
from pydantic import BaseModel

from src.apps.shared.generate_user_id import generate_user_id


class StudentIn(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: str
    personal_email: str
    gender: str
    contact: str
    date_of_enrolment: date
    profile_image: str
    enrolled_class: str
    home_address: str
    parent_id: UUID
    role: str
    student_id: int

class StudentOut(BaseModel):
    student_id: UUID
    
    class Config:
        extra_attributes = True