from uuid import UUID
from fastapi import APIRouter, status
from src.apps.school_management_system.teacher_management.services.teacher_attendance import TeacherAttendanceService as service


teacher_attendance_router = APIRouter(prefix='/teacher-attendances', tags=['Teacher Attendance'])

@teacher_attendance_router.get('/{teacher_id}/total', status_code=status.HTTP_200_OK)
async def get_all_attendances(teacher_id: str):
    return await service.get_all_attendances(teacher_id=teacher_id)


@teacher_attendance_router.get('/present/today', status_code=status.HTTP_200_OK)
async def get_all_present_today():
    return await service.get_all_present_today()

@teacher_attendance_router.post('/{teacher_id}/subjects/{subject_id}', status_code=status.HTTP_201_CREATED)
async def add_attendance(teacher_id: str, subject_id: UUID, present: bool = True, reason: str = ""):
    return await service.add_attendance(teacher_id=teacher_id, subject_id=subject_id, present=present, reason=reason)