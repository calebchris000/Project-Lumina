from uuid import UUID
from fastapi import APIRouter, status
from src.apps.school_management_system.class_management.schemas.school_class import (
    SchoolClassIn,
)
from src.core.enums.sort import SortBy
from src.apps.school_management_system.class_management.services.school_class import (
    SchoolClassService as service,
)


class_router = APIRouter(prefix="/classes", tags=["Class"])


@class_router.get("/", status_code=status.HTTP_200_OK)
async def get_all(
    filter_list: str = "",
    per_page: int = 10,
    page: int = 1,
    sort_by: SortBy = "ascending",
    order_by: str = "name",
    load_related: bool = False,
):
    return await service.get_all(
        filter_list=filter_list,
        per_page=per_page,
        page=page,
        sort_by=sort_by,
        order_by=order_by,
        load_related=load_related,
    )


@class_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_class(data_in: SchoolClassIn):
    return await service.create_class(data_in=data_in)


@class_router.put("/{class_id}", status_code=status.HTTP_200_OK)
async def update_class(class_id: UUID, data_in: SchoolClassIn):
    return await service.update_class(class_id=class_id, data_in=data_in)


@class_router.delete("/{class_id}", status_code=status.HTTP_200_OK)
async def delete_class(class_id: UUID):
    return await service.delete_class(class_id=class_id)
