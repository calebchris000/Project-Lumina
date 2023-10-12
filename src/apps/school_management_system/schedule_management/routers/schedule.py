# from datetime import datetime
# from uuid import UUID
# from fastapi import APIRouter, status
# from src.apps.school_management_system.teacher_management.schemas.teacher_schedule import (
#     TeacherScheduleIn,
# )
# from src.apps.school_management_system.schedule_management.services.schedule import (
#     TeacherScheduleService as service,
# )


# subject_schedule_router = APIRouter(prefix="/schedules", tags=["Subject Schedules"])


# @subject_schedule_router.get("/", status_code=status.HTTP_200_OK)
# async def get_all_schedules():
#     return await service.get_all_schedules()


# @subject_schedule_router.get("/{teacher_id}", status_code=status.HTTP_200_OK)
# async def get_schedules(teacher_id: int, from_date: datetime, to_date: datetime):
#     return await service.get_schedule(
#         teacher_id=teacher_id, from_date=from_date, to_date=to_date
#     )


# @subject_schedule_router.post("/{teacher_id}", status_code=status.HTTP_201_CREATED)
# async def create_schedule(
#     teacher_id: int, subject_id: UUID, from_date: datetime, to_date: datetime
# ):
#     return await service.create_schedule(
#         teacher_id=teacher_id,
#         subject_id=subject_id,
#         from_date=from_date,
#         to_date=to_date,
#     )


# @subject_schedule_router.put(
#     "/{schedule_id}/teacher/{teacher_id}/schedule-time", status_code=status.HTTP_200_OK
# )
# async def update_schedule_time(
#     schedule_id: UUID, teacher_id: int, data_in: TeacherScheduleIn
# ):
#     return await service.update_schedule_time(
#         schedule_id=schedule_id, teacher_id=teacher_id, data_in=data_in
#     )
    
# @subject_schedule_router.delete('/{schedule_id}', status_code=status.HTTP_200_OK)
# async def delete(schedule_id: UUID):
#     return await service.delete(schedule_id=schedule_id)