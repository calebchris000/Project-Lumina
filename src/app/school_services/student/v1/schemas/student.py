


from datetime import date
from uuid import UUID
from pydantic import BaseModel


class StudentIn(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: str
    email: str
    gender: str
    phone_number: str
    date_of_enrolment: date
    profile_image: str
    enrolled_class: str
    home_address: str
    parent_id: UUID
    role: str
    

class StudentOut(BaseModel):
    student_id: UUID
    
    class Config:
        extra_attributes = True