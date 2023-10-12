from fastapi import APIRouter, status
from src.core.enums.sort import SortBy
from src.apps.school_management_system.course_subject.schemas.course import CourseIn
from src.apps.school_management_system.course_subject.services.course import CourseService as service

course_router = APIRouter(prefix='/course', tags=['Course'])


@course_router.get('/', status_code=status.HTTP_200_OK)
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
    
@course_router.get('/total', status_code=status.HTTP_200_OK)
async def get_total():
    return await service.get_total()

@course_router.post('/', status_code=status.HTTP_201_CREATED)
async def create(data_in: CourseIn):
    return await service.create(data_in=data_in)


@course_router.put('/{course_id}', status_code=status.HTTP_200_OK)
async def update(course_id: str, data_in: CourseIn):
    return await service.update(course_id=course_id, data_in=data_in)


@course_router.delete('/{course_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(course_id: str):
    return await service.delete(course_id=course_id)