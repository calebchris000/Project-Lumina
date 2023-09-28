from fastapi import APIRouter
from src.app.school_services.teacher.v1.routers.teacher import teacher_router
from src.app.auth.v1.routers.signup import signup_router
from src.app.auth.v1.routers.login import login_router
from src.app.school_services.credentials.v1.routers.credential import credential_router
from src.app.school_services.student.v1.routers.student import student_router

router = APIRouter()


router.include_router(teacher_router)
router.include_router(student_router)
router.include_router(signup_router)
router.include_router(login_router)
router.include_router(credential_router)