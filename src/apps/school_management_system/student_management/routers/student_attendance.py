from uuid import UUID
from fastapi import APIRouter, status
from src.apps.school_management_system.student_management.services.student_attendance import StudentAttendanceService as service


student_attendance_router = APIRouter(prefix='/student-attendance', tags=['Student Attendance'])



@student_attendance_router.get('/{student_id}', status_code=status.HTTP_200_OK)
async def get_attendance_counts(student_id: str):
    return await service.get_counts(student_id=student_id)

@student_attendance_router.get('/present/today', status_code=status.HTTP_200_OK)
async def get_all_present_today():
    return await service.get_all_present_today()

@student_attendance_router.post('/{student_id}/subjects/{subject_id}', status_code=status.HTTP_201_CREATED)
async def add_attendance(student_id: str, subject_id: UUID, present: bool = True, reason: str = ""):
    return await service.add_attendance(student_id=student_id, subject_id=subject_id, present=present, reason=reason)