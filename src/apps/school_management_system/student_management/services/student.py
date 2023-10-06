from typing import Optional, Union
from uuid import UUID
from tortoise.models import Model
from src.apps.school_management_system.contact_management.models.user_contact import UserContact
from src.core.services.parse_and_list import parse_and_list, parse_and_return
from src.apps.shared.serialize_object import serialize_object
from src.apps.shared.generate_random_8 import generate_random_8
from src.apps.school_management_system.contact_management.schemas.school_contact import (
    SchoolContactIn,
)
from src.apps.school_management_system.contact_management.schemas.user_contact import (
    UserContactIn,
)
from src.apps.school_management_system.student_management.schemas.student import (
    StudentIn,
)
from src.apps.school_management_system.student_management.models.student import Student
from tortoise.expressions import Q
from src.core.schemas.response import IBaseResponse, IResponseMessage, PaginatedResponse
from src.exceptions import exception as exc


class StudentService(object):
    model = Student
    user_contact = UserContact

    @classmethod
    async def get_list(
        cls,
        filter_string: str,
        per_page: int = 10,
        page: int = 1,
        sort_by: str = "ascending",
        order_by: str = "first_name",
        load_related:bool = True
    ) -> PaginatedResponse:
        query = cls.model
        if filter_string:
            query = cls.model.filter(
                Q(first_name__icontains=filter_string)
                | Q(last_name__icontains=filter_string)
                | Q(home_address__icontains=filter_string)
                | Q(gender_icontains=filter_string)
                | Q(home_address__icontains=filter_string)
                | Q(student_id__icontains=filter_string)
            )
            
        return await parse_and_list(
            model=cls.model,
            query=query,
            per_page=per_page,
            page=page,
            sort_by=sort_by,
            order_by=order_by,
            load_related=load_related
        )

    @classmethod
    async def get_one(cls, student_id: str, load_related: bool = True) -> Union[dict, Model]:
        query = cls.model
        query = query.filter(student_id=student_id)
        
        return await parse_and_return(query=query, model=cls.model, load_related= load_related)
    @classmethod
    async def create_student(cls, data_in: StudentIn) -> Student:
        first_name = data_in.first_name
        last_name = data_in.last_name
        check_student = await cls.model.get_or_none(
            Q(first_name=first_name), Q(last_name=last_name)
        )

        if check_student:
            raise exc.DuplicateError(
                "Student with these names already exist",
                headers={"first_name": first_name, "last_name": last_name},
            )

        new_student = await cls.model.create(**data_in.model_dump(), student_id=generate_random_8(prefix='ST'))

        return new_student


    @classmethod
    async def create_user_contact(cls, student_id: str, data_in: UserContactIn):
        get_student = await cls.model.get_or_none(student_id=student_id).prefetch_related('usercontact')
        
        if not get_student:
            raise exc.NotFoundError('student not found')
        
        new_contact = await cls.user_contact.create(**data_in.model_dump(), student=get_student)
        contacts = await get_student.usercontact.all()
        # await get_student.save()
        return contacts
    @classmethod
    async def update_user_contact(cls, student_id: UUID, user_contact: UserContactIn) -> Student:
        find_student = await cls.model.get_or_none(id=student_id)

        if not find_student:
            raise exc.NotFoundError("student not found")
        
        contact = await cls.user_contact.get_or_none()
    @classmethod
    async def update_school_contact(
        cls, student_id: UUID, school_contact: SchoolContactIn
    ) -> Student:
        find_student = await cls.model.get_or_none(id=student_id)

        if not find_student:
            raise exc.NotFoundError("student not found")
        find_student.user_contact = school_contact
        await find_student.save()
        return find_student

    @classmethod
    async def delete_student(cls, student_id: str):
        find_student = await cls.model.filter(student_id=student_id).delete()

        if not find_student:
            raise exc.NotFoundError("student not found")

        return {"delete count": find_student}
