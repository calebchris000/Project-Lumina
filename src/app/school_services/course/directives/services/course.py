from uuid import UUID
from src.app.school_services.course.models.course import Course
from src.app.school_services.course.v1.schemas.course import CourseIn
from src.core.schemas.response import IBaseResponse, IResponseMessage
from src.exceptions import errors as exc


class CourseService(object):
    model = Course

    @classmethod
    async def get_list(cls) -> IBaseResponse:
        courses = await cls.model.all()
        return IBaseResponse(data=courses)

    @classmethod
    async def get_one(cls, id: UUID):
        get_course = await cls.model.get_or_none(id=id)

        if not get_course:
            raise exc.NotFoundError("Course not found")

        return IBaseResponse(data=get_course)

    @classmethod
    async def create(cls, data_in: CourseIn) -> IResponseMessage:
        find_course = await cls.model.get_or_none(name=data_in.name)

        if find_course:
            raise exc.DuplicateError(f"{data_in.name} already exist")

        await cls.model.create(**data_in.model_dump())

        return IResponseMessage(message="course created")

    @classmethod
    async def update(cls, id: UUID, data_in: CourseIn):
        find_course = await cls.model.get_or_none(id=id)
        if not find_course:
            raise exc.NotFoundError("course not found")

        await find_course.update_from_dict(data_in.model_dump())

        return IResponseMessage(message="update successful")
    
    
    @classmethod
    async def delete(cls, id: UUID):
        course_count = await cls.model.filter(id=id).delete()
        
        if not course_count:
            raise exc.NotFoundError('course not found')
        
        return {'delete count': course_count}