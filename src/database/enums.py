
from enum import Enum


class GENDERS(Enum):
    MALE = 'male'
    FEMALE = 'female'
    
class ROLES(Enum):
    SUPERUSER = 'superuser'
    MANAGER = 'manager'
    AUDITOR = 'auditor'
    EMPLOYEE = 'employee'
    GUEST = 'guest'