

from fastapi import APIRouter, status, Depends
from src.app.auth.directives.services.signup import SignupService

from src.app.auth.v1.schemas.signup import SignupIn

signup_router = APIRouter(prefix='/protected/signup', tags=['Signup'])
service = SignupService

@signup_router.post('/')
async def signup(data_in: SignupIn):
    return await SignupService.signup_User(data_in=data_in)