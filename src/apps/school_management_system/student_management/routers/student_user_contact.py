from fastapi import APIRouter, status
from src.apps.school_management_system.contact_management.schemas.user_contact import UserContactIn
from src.apps.school_management_system.student_management.services.student import StudentService as service



student_user_contact = APIRouter(prefix='/user_contact', tags=['User Contact'])




@student_user_contact.post('/{student_id}', status_code=status.HTTP_201_CREATED)
async def create_user_contact(student_id: int, data_in: UserContactIn):
    return await service.create_user_contact(student_id=student_id, data_in=data_in)