from uuid import UUID
from src.apps.school_management_system.course_subject.models.course import Course
from src.apps.school_management_system.course_subject.models.subject import Subject
from src.apps.shared.generate_random_8 import generate_random_8
from src.apps.school_management_system.teacher_management.schemas.teacher import (
    TeacherIn,
)
from src.core.services.parse_and_list import parse_and_list, parse_and_return
from src.core.enums.sort import SortBy
from src.apps.school_management_system.teacher_management.models.teacher import Teacher
from tortoise.expressions import Q
from src.exceptions import exception as exc


class TeacherService(object):
    model = Teacher
    subject_model = Subject
    course_model = Course
    @classmethod
    async def get_all(
        cls,
        filter_string: str = "",
        per_page: int = 10,
        page: int = 1,
        sort_by: SortBy = "ascending",
        order_by: str = "first_name",
        load_related: bool = True,
    ):
        query = cls.model
        if filter_string:
            query = query.filter(
                Q(first_name__icontains=filter_string)
                | Q(last_name__icontains=filter_string)
                | Q(years_of_experience__icontains=filter_string)
            )
        return await parse_and_list(
            model=cls.model,
            query=query,
            per_page=per_page,
            page=page,
            sort_by=sort_by,
            order_by=order_by,
            load_related=load_related,
        )

    @classmethod
    async def get_one(cls, teacher_id: int, load_related: bool = True):
        query = cls.model.filter(teacher_id=teacher_id)

        return await parse_and_return(
            query=query, model=cls.model, load_related=load_related
        )

    @classmethod
    async def create_teacher(cls, data_in: TeacherIn):
        teacher = await cls.model.filter(
            Q(first_name=data_in.first_name), Q(last_name=data_in.last_name)
        )
        if teacher:
            raise exc.DuplicateError(
                f"{data_in.first_name} {data_in.last_name} already exists"
            )

        new_teacher = await cls.model.create(
            **data_in.model_dump(), teacher_id=generate_random_8()
        )

        return new_teacher
    
    @classmethod
    async def update_teacher(cls, teacher_id: int, data_in: TeacherIn):
        teacher = await cls.model.filter(teacher_id=teacher_id).first()
        
        if not teacher:
            raise exc.NotFoundError('Teacher not found')
        
        teacher.update_from_dict(data_in.model_dump(exclude_none=True))
        
        await teacher.save()        
        return teacher
    
    @classmethod
    async def delete_teacher(cls, teacher_id: int):
        teacher = await cls.model.filter(teacher_id=teacher_id).delete()
        if not teacher:
            raise exc.NotFoundError('teacher does not exist')
        
        return {'delete count': teacher}
    
    @classmethod
    async def add_subject(cls, teacher_id: int, subject_id: UUID, course_id: UUID):
        teacher = await cls.model.filter(teacher_id=teacher_id).first()
        
        if not teacher:
            raise exc.NotFoundError('teacher does not exist')
        
        
        subject = await teacher.subjects.all()
        
        if subject:
            raise exc.DuplicateError(f'{subject.name} already assigned to {teacher.first_name} {teacher.last_name}')
        
        get_subject = await cls.subject_model.filter(id=subject_id).first()
        if not get_subject:
            raise exc.NotFoundError('subject not found')
        get_subject.teacher = teacher
        await get_subject.save()
        return await teacher.subjects
        # await add_subject.save()
        # return teacher.subjects