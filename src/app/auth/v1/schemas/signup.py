



from typing import Optional
from pydantic import BaseModel


class SignupIn(BaseModel):
    first_name: str
    middle_name: Optional[str]
    last_name: str
    username: str
    email: str
    password: str
    

class SignUpOut(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str