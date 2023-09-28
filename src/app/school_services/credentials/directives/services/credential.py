


from uuid import UUID
from src.app.school_services.credentials.models.credentials import Credential
from src.app.school_services.credentials.v1.schemas.credential import CredentialIn
from src.exceptions import errors as exc
class CredentialService(object):
    model = Credential
    
    @classmethod
    async def create(cls, data_in: CredentialIn):
        username = await cls.model.get_or_none(username=data_in.username)
        
        if username:
            raise exc.DuplicateError(f'{username} already has an account')
        
        new_user = await cls.model.create(**data_in.model_dump())
        
        return {"message": f'Created User {data_in.username}'}
    
    
    @classmethod
    async def delete(cls, user_id: UUID):
        user = await cls.model.filter(user_id=user_id).delete()
        
        if not user:
            raise exc.NotFoundError('User does not exist')
        
        return {'delete count': user}