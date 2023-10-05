import json
from uuid import UUID
from src.apps.school_management_system.class_management.models.school_class import (
    SchoolClass,
)
from src.apps.shared.serialize_object import serialize_object
from src.core.schemas.response import IBaseResponse
from src.apps.school_management_system.student_management.models.student import Student
from src.apps.school_management_system.student_management.models.student_attendance import (
    StudentAttendance,
)
from src.exceptions import exception as exc


class StudentAttendanceService(object):
    attendance_model = StudentAttendance
    student_model = Student
    class_model = SchoolClass

    @classmethod
    async def get_counts(cls, student_id: int):
        get_student = await cls.student_model.get_or_none(
            student_id=student_id
        ).prefetch_related("studentattendance")

        if not get_student:
            raise exc.NotFoundError("student not found")

        attendances = await get_student.studentattendance.all()

        return IBaseResponse(data=len(attendances))

    @classmethod
    async def add_attendance(
        cls, student_id: int, class_id: UUID, present: bool = True, reason: str = ""
    ):
        student = await cls.student_model.get_or_none(student_id=student_id)

        if not student:
            raise exc.NotFoundError("student not found")

        school_class = await cls.class_model.get_or_none(id=class_id)
        if not school_class:
            raise exc.NotFoundError("class not found")
        student = await cls.attendance_model.create(
            student_id=student_id, present=present, reason=reason, school_class_id=school_class.id
        )

        return student
