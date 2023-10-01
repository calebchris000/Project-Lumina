


import datetime
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime
from src.apps.shared.generate_random_8 import generate_random_8


class StudentIn(BaseModel):
    first_name: str = 'Caleb'
    last_name: str = 'Nwaizu'
    date_of_birth: datetime
    user_contact: str
    school_contact: str
    gender: str = 'male'
    date_of_enrollment: datetime
    profile_image: str
    enrolled_class: UUID = "318d71ee-7d5d-48c4-b341-b3246c78260e"
    home_address: str
    role: str ='guest'

class StudentOut(BaseModel):
    student_id: UUID
    
    class Config:
        extra_attributes = True