


from apps.school_management_system.attendance_tracking.enums.AttendanceStatus import AttendanceStatus
from database.model import BaseModel
from tortoise import fields

class StudentAttendance(BaseModel):
    student_id = fields.ForeignKeyField('models.Student', on_delete='CASCADE')
    status = fields.CharEnumField(AttendanceStatus, default=AttendanceStatus.NOT_RECORDED)