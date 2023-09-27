from fastapi import APIRouter, status



teacher_router = APIRouter(prefix='/teachers', tags=['Teachers'])


@teacher_router.get('/', status_code=status.HTTP_200_OK)
async def get_list():
    return {'message': "Teachers"}