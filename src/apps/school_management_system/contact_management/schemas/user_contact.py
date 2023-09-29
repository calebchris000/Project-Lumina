
from uuid import UUID
from pydantic import BaseModel


class UserContactIn(BaseModel):
    user_id: UUID
    home: int
    office: int
    email_address: str