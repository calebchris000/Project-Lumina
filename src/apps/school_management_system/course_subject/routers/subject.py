from fastapi import APIRouter, status
from src.apps.school_management_system.course_subject.schemas.subject import SubjectIn
from src.core.enums.sort import SortBy
from src.apps.school_management_system.course_subject.services.subject import (
    SubjectService as service,
)


subject_router = APIRouter(prefix="/subject", tags=["Subject"])


@subject_router.get("/", status_code=status.HTTP_200_OK)
async def get_list(
    filter_list: str = "",
    per_page: int = 10,
    page: int = 1,
    sort_by: SortBy = "ascending",
    order_by: str = "first_name",
    load_related: bool = True,
):
    return await service.get_list(
        filter_list=filter_list,
        per_page=per_page,
        page=page,
        sort_by=sort_by,
        order_by=order_by,
        load_related=load_related,
    )

@subject_router.post('/', status_code=status.HTTP_201_CREATED)
async def create_subject(data_in: SubjectIn):
    return await service.create(data_in=data_in)