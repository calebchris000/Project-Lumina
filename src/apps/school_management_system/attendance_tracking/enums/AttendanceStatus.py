from enum import Enum


class AttendanceStatus(Enum):
    PRESENT = "present"
    ABSENT = "absent"
    LATE = "late"
    NOT_RECORDED = 'not recorded'
