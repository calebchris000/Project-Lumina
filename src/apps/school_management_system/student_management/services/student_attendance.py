import json
from uuid import UUID
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

    @classmethod
    async def get_counts(cls, student_id: int):
        get_student = await cls.student_model.get_or_none(student_id=student_id)

        if not get_student:
            raise exc.NotFoundError("student not found")

        attendances = await cls.attendance_model.filter(student_id=student_id)

        if not attendances:
            return IBaseResponse(data="0")
        
        attendances_list = serialize_object(attendances)

        return IBaseResponse(data=attendances_list)

    @classmethod
    async def add_attendance(cls, student_id: int):
        student = await cls.student_model.get_or_none(student_id=student_id)

        if not student:
            raise exc.NotFoundError("student not found")

        student = await cls.attendance_model.create(
             student_id=student_id, status="present"
         )

        return student
