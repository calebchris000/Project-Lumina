from uuid import UUID
from src.apps.school_management_system.teacher_management.models.teacher import Teacher
from src.core.enums.sort import SortBy
from src.core.services.parse_and_list import parse_and_list
from src.apps.school_management_system.teacher_management.schemas.teacher_qualification import (
    TeacherQualificationIn,
)
from src.apps.school_management_system.teacher_management.models.teacher_qualification import (
    TeacherQualification,
)
from src.exceptions import exception as exc
from tortoise.expressions import Q


class TeacherQualificationService(object):
    model = TeacherQualification
    teacher_model = Teacher

    @classmethod
    async def get_teacher_qualifications(
        cls,
        teacher_id: int,
        filter_list: str = "",
        per_page: int = 10,
        page: int = 1,
        sort_by: SortBy = "ascending",
        order_by: str = "title",
        load_related: bool = True,
    ):
        query = cls.model
        if filter_list:
            query = query.filter(
                Q(teacher_id=teacher_id),
                Q(title__icontains=filter_list)
                | Q(institution__icontains=filter_list)
                | Q(year_completed__icontains=filter_list),
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
    async def add_qualification(cls, teacher_id: int, data_in: TeacherQualificationIn):
        teacher = await cls.teacher_model.filter(teacher_id=teacher_id).first()

        if not teacher:
            raise exc.NotFoundError("teacher not found")

        new_qualification = await cls.model.create(
            **data_in.model_dump(), teacher_id=teacher_id
        )

        return new_qualification

    @classmethod
    async def update_qualification(
        cls, teacher_id: int, data_in: TeacherQualificationIn
    ):
        teacher = await cls.teacher_model.filter(teacher_id=teacher_id).first()

        if not teacher:
            raise exc.NotFoundError("teacher not found")

        qualification = await cls.model.filter(teacher_id=teacher_id).first()
        if not qualification:
            raise exc.NotFoundError("qualification not found")

        qualification.update_from_dict(data_in.model_dump(exclude_none=True))
        await qualification.save()
        return qualification

    @classmethod
    async def delete_qualification(cls, qualification_id: UUID):
        qualification = await cls.model.filter(id=qualification_id).delete()

        if not qualification:
            raise exc.NotFoundError("qualification not found")
        return {"delete count": qualification}
