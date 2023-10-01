from src.apps.shared.serialize_object import serialize_object
from src.apps.school_management_system.course_subject.models.subject import Subject
from src.apps.school_management_system.student_management.schemas.student_grade import (
    StudentGradeIn,
)
from src.core.schemas.response import IBaseResponse, IResponseMessage
from src.apps.school_management_system.student_management.models.student import Student
from src.apps.school_management_system.student_management.models.student_grade import (
    StudentGrade,
)
from src.exceptions import exception as exc
from tortoise.expressions import Q


class StudentGradeService(object):
    student_model = Student
    grade_model = StudentGrade
    subject_model = Subject

    @classmethod
    async def get_all_grades(cls, student_id: int):
        student = await cls.student_model.filter(student_id=student_id)

        if not student:
            raise exc.NotFoundError("student not found")

        grades_all = await cls.grade_model.filter(Q(student_id=student_id)).prefetch_related('student_id')

        parsed_list = serialize_object(grades_all)
        return IBaseResponse(data=parsed_list)

    @classmethod
    async def get_grade_for_subject(cls, student_id: int, subject_id: int):
        student = await cls.student_model.get_or_none(student_id=student_id)
        if not student:
            raise exc.NotFoundError("student not found")
        subject = await cls.subject_model.get_or_none(subject_id=subject_id)
        if not subject:
            raise exc.NotFoundError("subject not found")
        
        return subject.st

    @classmethod
    async def create(cls, data_in: StudentGradeIn):
        student = await cls.student_model.get_or_none(student_id=data_in.student_id)

        if not student:
            raise exc.NotFoundError("student not found")
        subject = await cls.subject_model.get_or_none(id=data_in.subject_id)

        if not subject:
            raise exc.NotFoundError("subject not found")

        new_grade = await cls.grade_model.create(**data_in.model_dump())
        return IResponseMessage(message=new_grade, status_code=201)

    @classmethod
    async def update(cls, data_in: StudentGradeIn):
        student = await cls.student_model.get_or_none(student_id=data_in.student_id)

        if not student:
            raise exc.NotFoundError("student not found")
        subject = await cls.subject_model.get_or_none(id=data_in.subject_id)

        if not subject:
            raise exc.NotFoundError("subject not found")

        updated_grade = await cls.grade_model.update_from_dict(
            data_in.model_dump(exclude_unset=True)
        )
        return IResponseMessage(message=updated_grade, status_code=201)

    @classmethod
    async def delete(cls, grade_id: int):
        grade = await cls.grade_model.filter(id=grade_id).delete()

        if not grade:
            raise exc.NotFoundError("grade does not exist")

        return {"delete count": grade}
