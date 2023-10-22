


import datetime
from uuid import UUID
from pydantic import BaseModel
from datetime import date, datetime
from src.apps.shared.generate_random_8 import generate_random_8


class StudentIn(BaseModel):
    first_name: str = 'John'
    last_name: str = 'Doe'
    date_of_birth: date
    user_contact: str = None
    gender: str = 'male'
    date_of_enrollment: date
    profile_image: str = None
    grade:str = '5'
    home_address: str
    role: str ='guest'

class StudentOut(BaseModel):
    student_id: UUID
    
    class Config:
        extra_attributes = True