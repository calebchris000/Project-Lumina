


from pydantic import BaseModel


class PaginatedResponse(BaseModel):
    previous_page: int | None
    next_page: int | None
    results: list
    count: int
    