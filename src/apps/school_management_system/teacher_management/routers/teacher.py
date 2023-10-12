from uuid import UUID
from fastapi import APIRouter, status
from src.apps.school_management_system.teacher_management.schemas.teacher import (
    TeacherIn,
)
from src.core.enums.sort import SortBy
from src.apps.school_management_system.teacher_management.services.teacher import (
    TeacherService as service,
)


teacher_router = APIRouter(prefix="/teachers", tags=["Teachers"])


@teacher_router.get("/", status_code=status.HTTP_200_OK)
async def get_all(
    filter_string: str = "",
    per_page: int = 10,
    page: int = 1,
    sort_by: SortBy = "ascending",
    order_by: str = "first_name",
    load_related: bool = True,
):
    return await service.get_all(
        filter_string=filter_string,
        per_page=per_page,
        page=page,
        sort_by=sort_by,
        order_by=order_by,
        load_related=load_related,
    )


@teacher_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_teacher(data_in: TeacherIn):
    return await service.create_teacher(data_in=data_in)


@teacher_router.put("/{teacher_id}", status_code=status.HTTP_200_OK)
async def update_teacher(teacher_id: str, data_in: TeacherIn):
    return await service.update_teacher(teacher_id=teacher_id, data_in=data_in)


@teacher_router.put(
    "/{teacher_id}/course/{course_id}/subjects/{subject_id}",
    status_code=status.HTTP_200_OK,
)
async def add_subject(teacher_id: str,subject_id: UUID):
    return await service.add_subject(
        teacher_id=teacher_id, subject_id=subject_id
    )


@teacher_router.delete("/{teacher_id}", status_code=status.HTTP_200_OK)
async def delete_teacher(teacher_id: str):
    return await service.delete_teacher(teacher_id=teacher_id)
