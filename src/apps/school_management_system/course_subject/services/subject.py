from src.apps.school_management_system.course_subject.models.subject import Subject
from src.apps.school_management_system.course_subject.schemas.subject import SubjectIn
from src.core.schemas.response import IBaseResponse, IResponseMessage
from src.exceptions import exception as exc


class SubjectService(object):
    model = Subject

    @classmethod
    async def get_list(cls):
        subjects = await cls.model.all()

        if not subjects:
            return IBaseResponse()

        return IBaseResponse(data=subjects)

    @classmethod
    async def create(cls, data_in: SubjectIn):
        get_subject = await cls.model.get_or_none(name=data_in.name)

        if get_subject:
            raise exc.DuplicateError(f"{get_subject.name} already exist")

        new_subject = await cls.model.create(**data_in.model_dump())

        return new_subject

    @classmethod
    async def update(cls, data_in: SubjectIn):
        get_subject = await cls.model.get_or_none(name=data_in.name)

        if not get_subject:
            raise exc.NotFoundError("subject not found")

        await get_subject.update_from_dict(data_in.model_dump(exclude_unset=True))
        return get_subject
    
    @classmethod
    async def delete(cls, subject_id: int):
        get_subject = await cls.model.filter(id=subject_id).delete()
        
        if not get_subject:
            raise exc.NotFoundError('subject not found')
        
        return {'delete count': get_subject}