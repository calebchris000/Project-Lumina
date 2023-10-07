import json
from uuid import UUID
from src.apps.school_management_system.course_subject.models.subject import Subject
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
    subject_model = Subject

    @classmethod
    async def get_counts(cls, student_id: str):
        get_student = await cls.student_model.get_or_none(
            student_id=student_id
        ).prefetch_related("student_classes")

        if not get_student:
            raise exc.NotFoundError("student not found")

        attendances = await get_student.student_classes.all()

        return IBaseResponse(data=len(attendances))

    @classmethod
    async def add_attendance(
        cls, student_id: str, subject_id: UUID, present: bool = True, reason: str = ""
    ):
        student = await cls.student_model.get_or_none(student_id=student_id)

        if not student:
            raise exc.NotFoundError("student not found")

        subject = await cls.subject_model.get_or_none(id=subject_id)
        if not subject:
            raise exc.NotFoundError("subject not found")
        print(f"student {student_id} subject {subject_id}")
        student = await cls.attendance_model.create(
            student_id=student_id,
            present=present,
            reason=reason,
            subject_id=subject_id,
        )

        return student
