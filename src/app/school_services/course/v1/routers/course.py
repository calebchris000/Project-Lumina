from uuid import UUID
from fastapi import APIRouter, status

from src.app.school_services.course.directives.services.course import CourseService as service
from src.app.school_services.course.v1.schemas.course import CourseIn


course_router = APIRouter(prefix='/course', tags=['Course'])




@course_router.get('/', status_code=status.HTTP_200_OK)
async def get_list():
    return await service.get_list()


@course_router.get('/{id}', status_code=status.HTTP_200_OK)
async def get_one(id: UUID):
    return await service.get_one(id=id)


@course_router.post('/', status_code=status.HTTP_201_CREATED)
async def create_course(data_in: CourseIn):
    return await service.create(data_in=data_in)


@course_router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(id: UUID):
    return await service.delete(id=id)