from src.core.schemas.response import IBaseResponse
from src.apps.school_management_system.teacher_management.models.teacher import Teacher
from src.apps.school_management_system.teacher_management.models.teacher_attendance import (
    TeacherAttendance,
)
from src.exceptions import exception as exc


class TeacherAttendanceService(object):
    model = TeacherAttendance
    teacher_model = Teacher

    @classmethod
    async def get_all_attendances(cls, teacher_id: int):
        teacher = await cls.teacher_model.filter(teacher_id=teacher_id)

        if not teacher:
            raise exc.NotFoundError("teacher not found")
        all_attendances = await cls.model.filter(teacher_id=teacher_id).count()

        return IBaseResponse(data=all_attendances)
    
    @classmethod
    async def add_attendance(cls, teacher_id: int, status: str = 'present'):
        teacher = await cls.teacher_model.filter(teacher_id=teacher_id).first()
        
        if not teacher:
            raise exc.NotFoundError('teacher not found')
        attendances = await cls.model.create(teacher=teacher, status=status)
        
        return attendances