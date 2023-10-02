from fastapi import APIRouter, status
from src.apps.school_management_system.course_subject.schemas.course import CourseIn
from src.apps.school_management_system.course_subject.services.course import CourseService as service

course_router = APIRouter(prefix='/course', tags=['Course'])


@course_router.get('/', status_code=status.HTTP_200_OK)
async def get_list():
    return await service.get_list()


@course_router.post('/', status_code=status.HTTP_201_CREATED)
async def create(data_in: CourseIn):
    return await service.create(data_in=data_in)


@course_router.put('/{course_id}', status_code=status.HTTP_200_OK)
async def update(course_id: int, data_in: CourseIn):
    return await service.update(course_id=course_id, data_in=data_in)


@course_router.delete('/{course_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(course_id: int):
    return await service.delete(course_id=course_id)