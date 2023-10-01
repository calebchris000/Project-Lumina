from tortoise.models import Model
from src.core.enums.sort import SortBy


async def parse_and_list(
    model: Model,
    query: Model,
    per_page: int = 10,
    page: int = 1,
    sort_by: SortBy = "ascending",
    order_by: str = None,
    load_related: bool = True,
):
    offset = (page - 1) * per_page

    query = query.all().offset(offset).limit(per_page)

    if sort_by == "ascending":
        query = query.order_by("created_at")
    elif sort_by == "descending":
        query = query.order_by("-created_at")

    if order_by:
        query = query.order_by(f"{order_by}")

    prefetch_list = set.union(
        model._meta.m2m_fields,
        model._meta.o2o_fields,
        model._meta.fk_fields,
        model._meta.backward_fk_fields,
        model._meta.backward_o2o_fields,
    )

    if load_related:
        query = query.prefetch_related(*prefetch_list)

    results = await query
    model_list = await model.all()
    prev_page = page - 1 if page > 1 else None
    next_page = page + 1 if (offset + per_page) < len(model_list) else None
    return {
        'previous_page': prev_page,
        'next_page': next_page,
        'results': results,
        'count': len(results)
    }
