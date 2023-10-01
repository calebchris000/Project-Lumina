from src.apps.shared.serialize_object import serialize_object
from src.apps.shared.generate_random_8 import generate_random_8
from src.apps.school_management_system.course_subject.schemas.course import CourseIn
from src.apps.school_management_system.course_subject.models.course import Course
from src.core.schemas.response import IBaseResponse, IResponseMessage
from src.exceptions import exception as exc


class CourseService(object):
    model = Course

    @classmethod
    async def get_list(cls):
        courses = await cls.model.all()

        if not courses:
            return IBaseResponse()

        courses = serialize_object(courses)

        return IBaseResponse(data=courses)
    
    @classmethod
    async def get_one(cls, course_id: int):
        course = await cls.model.get_or_none(course_id=course_id)
        
        if not course:
            raise exc.NotFoundError('course not found')
        
    @classmethod
    async def create(cls, data_in: CourseIn):
        find_course = await cls.model.get_or_none(name=data_in.name)

        if find_course:
            raise exc.DuplicateError(f"{find_course.name} already exist")

        new_course = await cls.model.create(
            **data_in.model_dump(), course_id=generate_random_8()
        )

        return new_course

    @classmethod
    async def update(cls, course_id: int, data_in: CourseIn):
        find_course = await cls.model.get_or_none(course_id=course_id)

        if not find_course:
            raise exc.NotFoundError("course not found")

        await find_course.update_from_dict(
            data_in.model_dump(exclude_unset=True)
        ).save()
        return find_course

    @classmethod
    async def delete(cls, course_id: int):
        get_course = await cls.model.filter(course_id=course_id).delete()

        if not get_course:
            raise exc.NotFoundError("course not found")

        return {"delete count": get_course}
