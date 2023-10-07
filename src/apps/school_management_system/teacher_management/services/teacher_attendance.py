from uuid import UUID
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
        teacher = await cls.teacher_model.filter(teacher_id=teacher_id)

        if not teacher:
            raise exc.NotFoundError("teacher not found")
        all_attendances = await cls.model.filter(teacher_id=teacher_id).count()

        return IBaseResponse(data=all_attendances)

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
