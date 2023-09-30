from typing import Optional
from uuid import UUID
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
    async def get_list(cls, filter_string: Optional[str] = ""):
        students = await cls.model.all()
        if filter_string:
            print(filter_string)
            students = await cls.model.filter(
                Q(first_name__in=filter_string)
                | Q(last_name__in=filter_string)
                | Q(email__in=filter_string)
                | Q(phone_number__in=filter_string)
                | Q(home_address__in=filter_string)
            )

            return IBaseResponse(data=students)
        return IBaseResponse(data=students)

    @classmethod
    async def create_student(cls, data_in: StudentIn):
        first_name, last_name = data_in.model_dump(
            exclude=[
                "date_of_birth",
                "email",
                "gender",
                "phone_number",
                "date_of_enrolment",
                "profile_image",
                "enrolled_class",
                "home_address",
                "parent_id",
                "role",
            ]
        )
        check_student = await cls.model.get_or_none(
            Q(first_name=first_name), Q(last_name=last_name)
        )

        if check_student:
            raise exc.DuplicateError(
                "Student with these names already exist", headers=f"{data_in.first}"
            )

        await cls.model.create(**data_in.model_dump())

        return IResponseMessage(message=f"student created successfully")

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
            raise exc.NotFoundError('student not found')
        
        return {'delete count': find_student}