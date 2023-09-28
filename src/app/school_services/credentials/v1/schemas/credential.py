from uuid import UUID
from pydantic import BaseModel



class CredentialIn(BaseModel):
    username: str
    password: str
    user_id: UUID