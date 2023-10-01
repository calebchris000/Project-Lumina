
from uuid import UUID
from pydantic import BaseModel


class UserContactIn(BaseModel):
    user_id: UUID
    home: int = 1234
    office: int = 1234
    email_address: str = 'caleb@mail'