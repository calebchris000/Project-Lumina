from fastapi import APIRouter
from src.apps.school_management_system.teacher_management.routers.teacher import teacher_router
from src.apps.authentication.v1.routers.signup import signup_router
from src.apps.authentication.v1.routers.login import login_router
from src.apps.school_management_system.student_management.routers.student import student_router
from src.apps.school_management_system.student_management.routers.student_attendance import student_attendance_router

router = APIRouter()

router.include_router(teacher_router)
router.include_router(student_router)
router.include_router(student_attendance_router)
router.include_router(signup_router)
router.include_router(login_router)