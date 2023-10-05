from tortoise.models import Model
from src.core.enums.sort import SortBy
from typing import Union

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
        splitted = [
            column.strip()
            for column in order_by.split(",")
            if column in model._meta.fields
        ]
        query = query.order_by(*splitted)

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
    items_list = []

    # print(model._meta.m2m_fields)
    if load_related and results:
        for result in results:
            items = {}

            for field in model._meta.m2m_fields:
                if hasattr(result, field):
                    items[field] = dict(getattr(result, field))
            for field in model._meta.o2o_fields:
                if hasattr(result, field):
                    items[field] = dict(getattr(result, field))
            for field in model._meta.fk_fields:
                if hasattr(result, field):
                    items[field] = (getattr(result, field))
            for field in model._meta.backward_fk_fields:
                if hasattr(result, field):
                    items[field] = list(getattr(result, field))
            for field in model._meta.backward_o2o_fields:
                if getattr(result, field):
                    items[field] = dict(getattr(result, field))
            items.update(dict(result))
            items_list.append(items)
    else:
        items_list = results
    prev_page = page - 1 if page > 1 else None
    next_page = page + 1 if per_page == len(results) else None
    return {
        "previous_page": prev_page,
        "next_page": next_page,
        "results": items_list,
        "count": len(results),
    }


async def parse_and_return(model: Model, query: Model, load_related: bool = True):
    query = query.first()
    prefetch_list = set.union(
        model._meta.m2m_fields,
        model._meta.o2o_fields,
        model._meta.fk_fields,
        model._meta.backward_fk_fields,
        model._meta.backward_o2o_fields,
    )
    query = query.prefetch_related(*prefetch_list)
    
    result = await query
    items = {}
    if load_related and result:
        for field in model._meta.m2m_fields:
            if hasattr(result, field):
                items[field] = dict(getattr(result, field))
        for field in model._meta.o2o_fields:
            if hasattr(result, field):
                items[field] = dict(getattr(result, field))
        for field in model._meta.fk_fields:
            if hasattr(result, field):
                items[field] = dict(getattr(result, field))
        for field in model._meta.backward_fk_fields:
            if hasattr(result, field):
                items[field] = list(getattr(result, field))
        for field in model._meta.backward_o2o_fields:
            if hasattr(result, field):
                items[field] = {} if not getattr(result, field) else dict(getattr(result, field))

        items.update(dict(result))

    else:
        items = result

    return {"results": items}
