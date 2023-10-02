from fastapi import APIRouter, status
from src.apps.school_management_system.teacher_management.services.teacher_attendance import TeacherAttendanceService as service


teacher_attendance_router = APIRouter(prefix='/attendance', tags=['Teacher Attendance'])



@teacher_attendance_router.get('/{teacher_id}/total', status_code=status.HTTP_200_OK)
async def get_all_attendances(teacher_id: int):
    return await service.get_all_attendances(teacher_id=teacher_id)


@teacher_attendance_router.post('/{teacher_id}', status_code=status.HTTP_201_CREATED)
async def add_attendance(teacher_id: int, status: str = 'present'):
    return await service.add_attendance(teacher_id=teacher_id, status=status)