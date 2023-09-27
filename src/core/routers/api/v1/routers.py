from fastapi import APIRouter
from src.app.school_services.teacher.v1.routers.teacher import teacher_router
from src.app.auth.v1.routers.signup import signup_router
from src.app.auth.v1.routers.login import login_router
router = APIRouter()



router.include_router(teacher_router)
router.include_router(signup_router)
router.include_router(login_router)