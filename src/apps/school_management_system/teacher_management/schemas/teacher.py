


from datetime import date
from decimal import Decimal
from typing import Union
from uuid import UUID
from pydantic import BaseModel


class TeacherIn(BaseModel):
    first_name: str = 'Daniel'
    last_name: str = 'Walmart'
    date_of_birth: date = '2005-12-28'
    gender: str = 'male'
    date_of_enrollment: date = '2023-12-12'
    profile_image: str = 'http'
    home_address: str = '121, Keystone Place'
    subject_taught: str = 'Chemistry'
    qualifications: str = "bachelor's degree in education"
    role: str = 'guest'
    years_of_experience: Decimal = '12.5'

class TeacherOut(BaseModel):
    teacher_id: UUID
    
    class Config:
        extra_attributes = True