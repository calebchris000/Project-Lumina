
from typing import Annotated
from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
login_router = APIRouter(prefix='/user/login', tags=['Login'])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

@login_router.post('/', status_code=status.HTTP_201_CREATED)
async def login(data_in: Annotated[OAuth2PasswordBearer, Depends(oauth2_scheme)]):
    return {"Bearer":data_in}

