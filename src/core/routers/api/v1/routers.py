from fastapi import APIRouter
from src.apps.school_services.teacher.v1.routers.teacher import teacher_router


router = APIRouter()



router.include_router(teacher_router)