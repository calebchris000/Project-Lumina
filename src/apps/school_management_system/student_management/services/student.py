from typing import Optional
from uuid import UUID
from src.core.services.parse_and_list import parse_and_list
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
from src.core.schemas.response import IBaseResponse, IResponseMessage
from src.exceptions import exception as exc


class StudentService(object):
    model = Student

    @classmethod
    async def get_list(
        cls,
        filter_string: Optional[str] = "",
        per_page: int = 10,
        page: int = 2,
        sort_by: str = "ascending",
        order_by: str = "first_name",
        load_related:bool = False
    ):
        query = cls.model
        if filter_string:
            query = await cls.model.filter(
                Q(first_name__in=filter_string)
                | Q(last_name__in=filter_string)
                | Q(email__in=filter_string)
                | Q(phone_number__in=filter_string)
                | Q(home_address__in=filter_string)
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
    async def get_one(cls, student_id: int):
        student = await cls.model.get_or_none(student_id=student_id)

        if not student:
            raise exc.NotFoundError("student not found")

    @classmethod
    async def create_student(cls, data_in: StudentIn):
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

        await cls.model.create(**data_in.model_dump(), student_id=generate_random_8())

        return IResponseMessage(
            status_code=201, message=f"student created successfully"
        )

    @classmethod
    async def update_user_contact(cls, student_id: UUID, user_contact: UserContactIn):
        find_student = await cls.model.get_or_none(id=student_id)

        if not find_student:
            raise exc.NotFoundError("student not found")

        find_student.user_contact = user_contact
        await find_student.save()
        return find_student

    @classmethod
    async def update_school_contact(
        cls, student_id: UUID, school_contact: SchoolContactIn
    ):
        find_student = await cls.model.get_or_none(id=student_id)

        if not find_student:
            raise exc.NotFoundError("student not found")
        find_student.user_contact = school_contact
        await find_student.save()
        return find_student

    @classmethod
    async def delete_student(cls, student_id: UUID):
        find_student = await cls.model.filter(id=student_id).delete()

        if not find_student:
            raise exc.NotFoundError("student not found")

        return {"delete count": find_student}
