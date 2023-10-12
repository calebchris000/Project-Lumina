from uuid import UUID
from fastapi import APIRouter, status
from src.apps.school_management_system.teacher_management.schemas.teacher_qualification import TeacherQualificationIn
from src.core.enums.sort import SortBy
from src.apps.school_management_system.teacher_management.services.teacher_qualification import (
    TeacherQualificationService as service,
)


teacher_qualification_router = APIRouter(
    prefix="/qualifications", tags=["Teacher Qualification"]
)


@teacher_qualification_router.get("/{teacher_id}", status_code=status.HTTP_200_OK)
async def get_qualifications(
    teacher_id: str,
    filter_list: str = "",
    per_page: int = 10,
    page: int = 1,
    sort_by: SortBy = "ascending",
    order_by: str = "title",
    load_related: bool = True,
):
    return await service.get_teacher_qualifications(
        teacher_id=teacher_id,
        filter_list=filter_list,
        per_page=per_page,
        page=page,
        sort_by=sort_by,
        order_by=order_by,
        load_related=load_related,
    )
    

@teacher_qualification_router.post('/{teacher_id}', status_code=status.HTTP_201_CREATED)
async def add_qualification(teacher_id: str, data_in: TeacherQualificationIn):
    return await service.add_qualification(teacher_id=teacher_id, data_in=data_in)


@teacher_qualification_router.put('/{teacher_id}', status_code=status.HTTP_200_OK)
async def update_qualification(teacher_id: str, data_in: TeacherQualificationIn):
    return await service.update_qualification(teacher_id=teacher_id, data_in=data_in)

@teacher_qualification_router.delete('/{qualification_id}', status_code=status.HTTP_200_OK)
async def delete_qualification(qualification_id: UUID):
    return await service.delete_qualification(qualification_id=qualification_id)