from math import ceil
from typing import List

from space_traders.client import Client
from space_traders.models import ApiError
from space_traders.models import Meta


async def paginator(
    client: Client,
    method: str,
    endpoint: str,
    limit: int = 20,
    page: int = 1,
    data: List | None = None,
    **kwargs,
) -> List | ApiError:
    params = {"limit": limit, "page": page}
    if "params" in kwargs.keys():
        params = kwargs.pop("params") | params
    if data is None:
        data = []
    r = await client.send(method, endpoint, params=params, **kwargs)
    if "error" in r.keys():
        return ApiError(**r)

    for response_data in r["data"]:
        data.append(response_data)

    meta = Meta(**r["meta"])
    pages = ceil(meta.total / meta.limit)
    if page < pages:
        response = await paginator(
            client, method, endpoint, limit, page + 1, data, **kwargs
        )
        if isinstance(response, list):
            data = response
    return data
