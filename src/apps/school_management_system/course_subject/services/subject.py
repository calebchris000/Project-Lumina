from src.apps.school_management_system.course_subject.models.course import Course
from src.core.enums.sort import SortBy
from src.core.services.parse_and_list import parse_and_list
from src.apps.school_management_system.course_subject.models.subject import Subject
from src.apps.school_management_system.course_subject.schemas.subject import SubjectIn
from src.core.schemas.response import IBaseResponse, IResponseMessage
from src.exceptions import exception as exc
from tortoise.expressions import Q


class SubjectService(object):
    model = Subject
    course_model = Course

    @classmethod
    async def get_list(
        cls,
        filter_list: str = "",
        per_page: int = 10,
        page: int = 1,
        sort_by: SortBy = "ascending",
        order_by: str = "first_name",
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
    async def create(cls, data_in: SubjectIn):
        get_subject = await cls.model.get_or_none(name=data_in.name)

        if get_subject:
            raise exc.DuplicateError(f"{get_subject.name} already exist")
        
        get_course = await cls.course_model.filter(id=data_in.course_id)
        if not get_course:
            raise exc.NotFoundError('course not found')
        new_subject = await cls.model.create(**data_in.model_dump())

        return new_subject

    @classmethod
    async def update(cls, data_in: SubjectIn):
        get_subject = await cls.model.get_or_none(name=data_in.name)

        if not get_subject:
            raise exc.NotFoundError("subject not found")

        await get_subject.update_from_dict(data_in.model_dump(exclude_unset=True))
        return get_subject

    @classmethod
    async def delete(cls, subject_id: int):
        get_subject = await cls.model.filter(id=subject_id).delete()

        if not get_subject:
            raise exc.NotFoundError("subject not found")

        return {"delete count": get_subject}
