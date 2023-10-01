from typing import Dict, List, Tuple, AnyStr, Union
from fastapi import APIRouter, status
from src.apps.school_management_system.student_management.schemas.student import StudentIn
from src.core.schemas.response import IBaseResponse
from src.apps.school_management_system.student_management.services.student import (
    StudentService as service,
)


student_router = APIRouter(prefix="/student", tags=["Student"])


@student_router.get("/", status_code=status.HTTP_200_OK)
async def get_list(filter_string: str = ""):
    return await service.get_list(filter_string=filter_string)


@student_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_student(data_in: StudentIn):
    return await service.create_student(data_in=data_in)
