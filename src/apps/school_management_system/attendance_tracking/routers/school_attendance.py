from datetime import date
from fastapi import APIRouter, status
from src.apps.school_management_system.attendance_tracking.schemas.teacher_attendance import TeacherSchoolAttendanceIn
from src.apps.school_management_system.attendance_tracking.services.school_attendance import (
    SchoolAttendanceService as service,
)
from src.core.enums.sort import SortBy


school_attendance_router = APIRouter(
    prefix="/school-attendances", tags=["School Attendance"]
)


@school_attendance_router.get("/teachers/{teacher_id}", status_code=status.HTTP_200_OK)
async def get_list(
    teacher_id: str,
    from_date: date = '1990-01-01',
    to_date: date = date.today(),
    per_page: int = 10,
    page: int = 1,
    sort_by: SortBy = SortBy.ASCENDING,
    order_by: str = "date_of_presence",
    load_related: bool = True,
):
    return await service.get_list(
        teacher_id=teacher_id,
        from_date=from_date,
        to_date=to_date,
        per_page=per_page,
        page=page,
        sort_by=sort_by,
        order_by=order_by,
        load_related=load_related,
    )

@school_attendance_router.post('/teachers/{teacher_id}', status_code=status.HTTP_200_OK)
async def add_teacher_attendance(data_in: TeacherSchoolAttendanceIn):
    return await service.add_teacher_attendance(data_in=data_in)