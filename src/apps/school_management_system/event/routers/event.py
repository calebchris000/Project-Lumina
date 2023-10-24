from datetime import datetime
from uuid import UUID
from fastapi import APIRouter, status
from src.apps.school_management_system.event.schemas.event import EventIn
from src.apps.school_management_system.event.services.event import EventService as service

event_router = APIRouter(prefix='/events', tags=['Events'])


@event_router.get('/', status_code=status.HTTP_200_OK)
async def get_upcoming_events_month(date: datetime = datetime.now()):
    return await service.get_upcoming_events_month(date=date)

@event_router.post('/', status_code=status.HTTP_201_CREATED)
async def create_event(data_in: EventIn):
    return await service.create_event(data_in=data_in)

@event_router.put('/{event_id}', status_code=status.HTTP_200_OK)
async def update_event(event_id: UUID, data_in: EventIn):
    return await service.update_event(event_id=event_id, data_in=data_in)

@event_router.delete('/{event_id}', status_code=status.HTTP_200_OK)
async def delete_event(event_id: UUID):
    return await service.delete_event(event_id=event_id)