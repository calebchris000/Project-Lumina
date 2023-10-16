from uuid import UUID
from src.apps.school_management_system.course_subject.models.subject import Subject
from src.apps.school_management_system.teacher_management.models.teacher import Teacher
from src.apps.school_management_system.class_management.schemas.school_class import (
    SchoolClassIn,
)
from src.core.services.parse_and_list import parse_and_list
from src.core.enums.sort import SortBy
from src.apps.school_management_system.class_management.models.school_class import (
    SchoolClass,
)
from tortoise.expressions import Q
from src.exceptions import exception as exc


class SchoolClassService(object):
    class_model = SchoolClass
    subject_model = Subject
    teacher_model = Teacher

    @classmethod
    async def get_all(
        cls,
        filter_list: str = "",
        per_page: int = 10,
        page: int = 1,
        sort_by: SortBy = "ascending",
        order_by: str = "name",
        load_related: bool = False,
    ):
        query = cls.class_model

        if filter_list:
            query = query.filter(
                Q(name__icontains=filter_list)
                | Q(size__icontains=filter_list)
                | Q(identifier__icontains=filter_list)
                | Q(description__icontains=filter_list)
            )

        return await parse_and_list(
            model=cls.class_model,
            query=query,
            per_page=per_page,
            page=page,
            sort_by=sort_by,
            order_by=order_by,
            load_related=load_related,
        )

    @classmethod
    async def create_class(cls, data_in: SchoolClassIn):
        school_class = await cls.class_model.filter(name=data_in.name)
        if school_class:
            raise exc.NotFoundError(f"{data_in.name} is already a class")

        new_class = await cls.class_model.create(**data_in.model_dump(exclude_none=True))
        return new_class

    @classmethod
    async def update_class(cls, class_id: UUID, data_in: SchoolClassIn):
        school_class = await cls.class_model.filter(id=class_id).first()
        if not school_class:
            raise exc.NotFoundError("class not found")

        await school_class.update_from_dict(data_in.model_dump(exclude_none=True))
        return school_class

    @classmethod
    async def delete_class(cls, class_id: UUID):
        school_class = await cls.class_model.filter(id=class_id).delete()

        if not school_class:
            raise exc.NotFoundError("class not found")

        return {"delete count": school_class}

    @classmethod
    async def attach_subject(cls, class_id: UUID, data_in: SchoolClassIn):
        subject = await cls.subject_model.filter(id=data_in.subject_id)

        if not subject:
            raise exc.NotFoundError("subject not found")

        school_class = await cls.class_model.filter(id=class_id).first()

        if not school_class:
            raise exc.NotFoundError("class not found")

        await school_class.update_from_dict(
            data_in.model_dump(exclude_none=True)
        ).save()
        return school_class
