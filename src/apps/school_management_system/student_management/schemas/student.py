


import datetime
from uuid import UUID
from pydantic import BaseModel
from datetime import date, datetime
from src.apps.shared.generate_random_8 import generate_random_8


class StudentIn(BaseModel):
    first_name: str = 'John'
    last_name: str = 'Doe'
    date_of_birth: date = '2001-12-28'
    user_contact: str
    school_contact: str
    gender: str = 'male'
    date_of_enrollment: date = date
    profile_image: str
    grade:str = '5'
    home_address: str
    role: str ='guest'

class StudentOut(BaseModel):
    student_id: UUID
    
    class Config:
        extra_attributes = True