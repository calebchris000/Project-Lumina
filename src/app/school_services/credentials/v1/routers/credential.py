from uuid import UUID
from fastapi import APIRouter, status
from src.app.school_services.credentials.directives.services.credential import CredentialService

from src.app.school_services.credentials.v1.schemas.credential import CredentialIn



credential_router = APIRouter(prefix='/credential', tags=['Credential'])
service = CredentialService

@credential_router.post('/', status_code=status.HTTP_201_CREATED)
async def create(data_in: CredentialIn):
    return await service.create(data_in=data_in)

@credential_router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(user_id: UUID):
    return await service.delete(user_id=user_id)