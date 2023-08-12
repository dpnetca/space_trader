from space_traders.client import Client
from space_traders.models import ApiError

from typing import List

from math import ceil

from space_traders.models.Meta import Meta


def paginator(
    client: Client,
    method: str,
    endpoint: str,
    limit: str = 20,
    page: str = 1,
    data: List = [],
    **kwargs
) -> List:
    params = {"limit": limit, "page": page}
    if "params" in kwargs.keys():
        params = kwargs.pop("params") | params
    r = client.send(method, endpoint, params=params, **kwargs)
    if "error" in r.keys():
        return ApiError(**r)

    for response_data in r["data"]:
        data.append(response_data)

    meta = Meta(**r["meta"])
    pages = ceil(meta.total / meta.limit)
    if page < pages:
        data = paginator(
            client, method, endpoint, limit, page + 1, data, **kwargs
        )
    return data
