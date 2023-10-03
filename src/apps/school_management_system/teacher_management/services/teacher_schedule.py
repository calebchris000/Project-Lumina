from uuid import UUID
from src.apps.school_management_system.teacher_management.schemas.teacher_schedule import (
    TeacherScheduleIn,
)
from src.apps.school_management_system.course_subject.models.subject import Subject
from src.apps.school_management_system.teacher_management.models.teacher import Teacher
from src.apps.school_management_system.teacher_management.models.teacher_schedule import (
    TeacherSchedule,
)
from src.exceptions import exception as exc
from datetime import datetime
from tortoise.expressions import Q


class TeacherScheduleService(object):
    teacher_model = Teacher
    subject_model = Subject
    model = TeacherSchedule
    
    @classmethod
    async def get_all_schedules(cls):
        schedules = await cls.model.all()
        return schedules
    @classmethod
    async def get_schedule(
        cls, teacher_id: int, from_date: datetime, to_date: datetime
    ):
        teacher = await cls.teacher_model.filter(teacher_id=teacher_id).first()

        if not teacher:
            raise exc.NotFoundError("teacher not found")

        schedules = await cls.model.filter(
            Q(from_date__gte=from_date), Q(to_date__lte=to_date)
        )

        return schedules

    @classmethod
    async def create_schedule(
        cls, teacher_id: int, subject_id: UUID, from_date: datetime, to_date: datetime
    ):
        teacher = await cls.teacher_model.filter(teacher_id=teacher_id).first()

        if not teacher:
            raise exc.NotFoundError("teacher not found")

        subject = await cls.subject_model.filter(id=subject_id).first()

        if not subject:
            raise exc.NotFoundError("subject not found")

        check_schedule = await cls.model.get_or_none(
            Q(teacher=teacher), Q(subject=subject)
        )

        if check_schedule:
            raise exc.NotFoundError(
                f"{subject.name} has already been scheduled around the time {check_schedule.from_date} to {check_schedule.to_date} for {teacher.first_name} {teacher.last_name}"
            )

        new_schedule = await cls.model.create(
            teacher=teacher, subject=subject, from_date=from_date, to_date=to_date
        )

        return new_schedule

    @classmethod
    async def update_schedule_time(
        cls, teacher_id: int, schedule_id: UUID, data_in: TeacherScheduleIn
    ):
        teacher = await cls.teacher_model.filter(teacher_id=teacher_id).first()
        if not teacher:
            raise exc.NotFoundError("teacher not found")

        schedule = await cls.model.filter(id=schedule_id).first()

        if not schedule:
            raise exc.NotFoundError("schedule not found")

        schedule.update_from_dict(data_in.model_dump(exclude_none=True, exclude_unset=True))
        await schedule.save()
        return schedule
