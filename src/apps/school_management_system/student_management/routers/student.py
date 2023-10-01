from typing import Dict, List, Tuple, AnyStr, Union
from fastapi import APIRouter, status
from src.core.enums.sort import SortBy
from src.apps.school_management_system.student_management.schemas.student import (
    StudentIn,
)
from src.core.schemas.response import IBaseResponse
from src.apps.school_management_system.student_management.services.student import (
    StudentService as service,
)


student_router = APIRouter(prefix="/student", tags=["Student"])


@student_router.get("/", status_code=status.HTTP_200_OK)
async def get_list(
    filter_string: str = "",
    per_page: int = 10,
    page: int = 1,
    sort_by: SortBy = SortBy.ASCENDING,
    order_by: str = "first_name",
    load_related: bool = True,
):
    return await service.get_list(
        filter_string=filter_string,
        per_page=per_page,
        page=page,
        sort_by=sort_by,
        order_by=order_by,
        load_related=load_related,
    )


@student_router.get("/{student_id}", status_code=status.HTTP_200_OK)
async def get_one(student_id: int, load_related: bool = True):
    return await service.get_one(student_id=student_id, load_related=load_related)


@student_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_student(data_in: StudentIn):
    return await service.create_student(data_in=data_in)
