from typing import AnyStr, Dict, List, Tuple, Type, Union
from pydantic import BaseModel
from tortoise.models import Model
class ITotalCount(BaseModel):
    count: int


class IResponseMessage(BaseModel):
    status_code: int = 200
    message: str = "Accepted"


class IBaseResponse(BaseModel):
    status_code: int = 200
    data: Union[Dict, List, Tuple, AnyStr] = []
    headers: Union[Dict, List] = []

class PaginatedResponse(BaseModel):
    previous_page: int | None
    next_page: int | None
    results: Type[Model]
    count: int
    