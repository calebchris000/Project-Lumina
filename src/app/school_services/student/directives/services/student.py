from typing import Optional
from src.app.school_services.student.v1.schemas.student import StudentIn
from src.app.school_services.student.models.student import Student
from tortoise.expressions import Q
from src.core.schemas.response import IBaseResponse, IResponseMessage
from src.exceptions import errors as exc


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
