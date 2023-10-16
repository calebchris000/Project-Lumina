from datetime import datetime
from uuid import UUID
from tortoise.expressions import Q
from src.apps.school_management_system.course_subject.models.subject import Subject
from src.core.schemas.response import IBaseResponse
from src.apps.school_management_system.teacher_management.models.teacher import Teacher
from src.apps.school_management_system.teacher_management.models.teacher_attendance import (
    TeacherAttendance,
)
from src.exceptions import exception as exc


class TeacherAttendanceService(object):
    model = TeacherAttendance
    teacher_model = Teacher
    subject_model = Subject

    @classmethod
    async def get_all_attendances(cls, teacher_id: str):
        teacher = await cls.teacher_model.filter(teacher_id=teacher_id).prefetch_related('teacher_attendances')

        if not teacher:
            raise exc.NotFoundError("teacher not found")
        all_attendances = await cls.model.filter(teacher_id=teacher_id).count()

        return IBaseResponse(data=all_attendances)

    @classmethod
    async def get_all_present_today(cls):
        current_day = datetime.now().strftime("%d")
        all_attendances = await cls.model.filter(
            Q(created_at__day=current_day), Q(present=True)
        )
        unique_teacher_id = set()
        unique_students = []

        for attendant in all_attendances:
            teacher_id = attendant.teacher_id
            if teacher_id not in unique_teacher_id:
                unique_teacher_id.add(teacher_id)
                unique_students.append(attendant)
        return IBaseResponse(data=len(unique_students))

    @classmethod
    async def add_attendance(
        cls, teacher_id: str, subject_id: UUID, present: bool = True, reason: str = ""
    ):
        teacher = await cls.teacher_model.filter(teacher_id=teacher_id).first()

        if not teacher:
            raise exc.NotFoundError("teacher not found")

        subject = await cls.subject_model.get_or_none(id=subject_id)
        if not subject:
            raise exc.NotFoundError("subject not found")
        attendances = await cls.model.create(
            teacher=teacher, subject=subject, present=present, reason=reason
        )

        return attendances
