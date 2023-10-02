


from src.apps.school_management_system.attendance_tracking.enums.AttendanceStatus import AttendanceStatus
from src.database.model import BaseModel
from tortoise import fields

class TeacherAttendance(BaseModel):
    teacher = fields.ForeignKeyField('models.Teacher', to_field='teacher_id', related_name='attendances')
    status = fields.CharEnumField(AttendanceStatus, default=AttendanceStatus.NOT_RECORDED)