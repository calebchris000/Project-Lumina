from fastapi import APIRouter, status

from src.apps.school_management_system.student_management.services.student_grade import StudentGradeService as service



student_grade_router = APIRouter(prefix='/grades', tags=['Student Grade'])


@student_grade_router.get('/{student_id}', status_code=status.HTTP_200_OK)
async def get_all(student_id: int):
    return await service.get_all_grades(student_id=student_id)