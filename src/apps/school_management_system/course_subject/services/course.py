from src.apps.school_management_system.class_management.models.school_class import (
    SchoolClass,
)
from src.core.services.parse_and_list import parse_and_list
from src.core.enums.sort import SortBy
from src.apps.shared.serialize_object import serialize_object
from src.apps.shared.generate_random_8 import generate_random_8
from src.apps.school_management_system.course_subject.schemas.course import CourseIn
from src.apps.school_management_system.course_subject.models.course import Course
from src.core.schemas.response import IBaseResponse, IResponseMessage
from src.exceptions import exception as exc
from tortoise.expressions import Q


class CourseService(object):
    model = Course
    class_model = SchoolClass

    @classmethod
    async def get_list(
        cls,
        filter_list: str = "",
        per_page: int = 10,
        page: int = 1,
        sort_by: SortBy = "ascending",
        order_by: str = "name",
        load_related: bool = True,
    ):
        query = cls.model

        if filter_list:
            query = query.filter(
                Q(name__in=filter_list) | Q(description_in=filter_list)
            )

        return await parse_and_list(
            query=query,
            model=cls.model,
            per_page=per_page,
            page=page,
            sort_by=sort_by,
            order_by=order_by,
            load_related=load_related,
        )

    @classmethod
    async def get_one(cls, course_id: int):
        course = await cls.model.get_or_none(course_id=course_id)

        if not course:
            raise exc.NotFoundError("course not found")

    @classmethod
    async def create(cls, data_in: CourseIn):
        course = await cls.model.get_or_none(name=data_in.name)

        if course:
            raise exc.DuplicateError(f"{course.name} already exist")

        new_course = await cls.model.create(**data_in.model_dump())

        return new_course
    
    @classmethod
    async def get_total(cls):
        courses = await cls.model.all().count()
        
        return IBaseResponse(data=courses)
    @classmethod
    async def update(cls, course_id: str, data_in: CourseIn):
        course = await cls.model.get_or_none(id=course_id)

        if not course:
            raise exc.NotFoundError("course not found")

        school_class = await cls.class_model.get_or_none(id=data_in.class_id)
        data = {
            **data_in.model_dump(exclude_none=True),
            "school_class_id": school_class.id,
        }
        if not school_class:
            raise exc.NotFoundError("class not found")
        await course.update_from_dict(data).save()
        return course

    @classmethod
    async def delete(cls, course_id: int):
        get_course = await cls.model.filter(course_id=course_id).delete()

        if not get_course:
            raise exc.NotFoundError("course not found")

        return {"delete count": get_course}
