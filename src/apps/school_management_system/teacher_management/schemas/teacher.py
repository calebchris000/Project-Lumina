


from datetime import date
from decimal import Decimal
from uuid import UUID
from pydantic import BaseModel

from apps.shared.generate_user_id import generate_user_id


class TeacherIn(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: str
    email: str
    gender: str
    contact: str
    date_of_enrolment: date
    profile_image: str
    enrolled_class: str
    home_address: str
    subject_taught: UUID
    qualifications: str
    role: str
    years_of_experience: Decimal
    teacher_id: int

class TeacherOut(BaseModel):
    teacher_id: UUID
    
    class Config:
        extra_attributes = True