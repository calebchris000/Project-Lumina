from datetime import date
from src.apps.school_management_system.teacher_management.models.teacher import Teacher
from src.apps.school_management_system.attendance_tracking.schemas.teacher_attendance import TeacherSchoolAttendanceIn
from src.core.services.parse_and_list import parse_and_list
from src.core.enums.sort import SortBy
from src.apps.school_management_system.attendance_tracking.models.school_attendance import (
    SchoolAttendance,
)
from tortoise.expressions import Q
from src.exceptions import exception as exc

class SchoolAttendanceService(object):
    model = SchoolAttendance
    teacher_model = Teacher

    @classmethod
    async def get_list(
        cls,
        teacher_id: str,
        from_date: date,
        to_date: date,
        per_page: int = 10,
        page: int = 1,
        sort_by: SortBy = SortBy.ASCENDING,
        order_by: str = "from_date",
        load_related: bool = True,
    ):
        query = cls.model
        teacher = await cls.teacher_model.filter(teacher_id=teacher_id).first()
        if not teacher:
            raise exc.NotFoundError('teacher not found') 
        if from_date and to_date:
            query = query.filter(
                Q(teacher_id=teacher_id),
                Q(date_of_presence__gte=from_date),
                Q(date_of_presence__lte=to_date),
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
    async def add_teacher_attendance(
        cls, data_in: TeacherSchoolAttendanceIn
    ):
        teacher = (
            await cls.teacher_model.filter(teacher_id=data_in.teacher_id)
            .first()
            .prefetch_related("teacher_attendances")
        )

        if not teacher:
            raise exc.NotFoundError('teacher not found')
        
        attendances = await teacher.teacher_attendances.filter(date_of_presence=data_in.date_of_presence).first()
        
        if attendances:
            raise exc.DuplicateError(f'{attendances.date_of_presence} has already been recorded')
        
        new_attendance = await cls.model.create(**data_in.model_dump(exclude_none=True))
        return new_attendance
        
