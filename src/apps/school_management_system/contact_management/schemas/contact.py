
from uuid import UUID
from pydantic import BaseModel


class ContactIn(BaseModel):
    user_id: UUID
    home: int
    office: int
    email_address: str