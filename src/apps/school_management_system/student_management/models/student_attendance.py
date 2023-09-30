


from src.apps.school_management_system.attendance_tracking.enums.AttendanceStatus import AttendanceStatus
from src.database.model import BaseModel
from tortoise import fields

class StudentAttendance(BaseModel):
    student = fields.ForeignKeyField('models.Student', on_delete='CASCADE', to_field='student_id')
    status = fields.CharEnumField(AttendanceStatus, default=AttendanceStatus.NOT_RECORDED)