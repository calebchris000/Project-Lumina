

from fastapi import APIRouter, status, Depends
from src.apps.authentication.directives.services.signup import SignupService

from src.apps.authentication.v1.schemas.signup import SignupIn

signup_router = APIRouter(prefix='/protected/signup', tags=['Signup'])
service = SignupService

@signup_router.post('/')
async def signup(data_in: SignupIn):
    return await service.signup_user(data_in=data_in)