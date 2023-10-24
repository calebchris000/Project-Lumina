import calendar
from datetime import datetime, timedelta
from uuid import UUID
from src.core.schemas.response import IResponseMessage
from src.apps.school_management_system.event.schemas.event import EventIn
from src.apps.shared.month_number_to_string import month_number_to_string
from src.apps.school_management_system.event.models.event import Event
from tortoise.expressions import Q
from src.exceptions import exception as exc


class EventService(object):
    model = Event

    @classmethod
    async def get_upcoming_events_month(cls, date: datetime):
        
        current_date = datetime.now()
        if not current_date.month == date.month:
            current_date = date
        tomorrow_date = datetime(year=current_date.year, month=current_date.month, day=current_date.day) + timedelta(days=1)
        days_in_month = calendar.monthrange(current_date.year, current_date.month)[1]
        end_date = datetime(
            year=current_date.year, month=current_date.month, day=days_in_month
        )
        events = await cls.model.filter(
            Q(date__gte=tomorrow_date),
            Q(date__lte=end_date),
        )

        if not events:
            month = month_number_to_string(current_date.month)
            raise exc.NotFoundError(f"no upcoming events for {month}")

        return events

    @classmethod
    async def create_event(cls, data_in: EventIn):
        event = await cls.model.get_or_none(Q(name=data_in.name), Q(date=data_in.date))

        if event:
            raise exc.DuplicateError(
                f"{event.name} is already assigned with the date: {event.date}. Please select another date"
            )

        event_is_younger_than_date = data_in.date <= datetime.now()

        if event_is_younger_than_date:
            raise exc.BadDataError(
                "Error: Event creation date cannot be set to a date in the past. Please select a date that is equal to or later than the current date."
            )
        new_event = await cls.model.create(**data_in.model_dump())
        return new_event

    @classmethod
    async def update_event(cls, event_id: UUID, data_in: EventIn):
        event = await cls.model.get_or_none(id=event_id)
        if not event:
            raise exc.NotFoundError('event cannot be found')
        
        await event.update_from_dict(data_in.model_dump(exclude_unset=True)).save()
        return event
    
    @classmethod
    async def delete_event(cls, event_id: UUID):
        event = await cls.model.get_or_none(id=event_id)
        if not event:
            raise exc.NotFoundError('event not found or already deleted')
        
        await event.delete()
        return IResponseMessage(status_code=204, message='Event deleted')