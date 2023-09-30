from uuid import UUID

from pydantic import BaseModel


class SchoolContactIn(BaseModel):
    user_id: UUID
    email_address: str