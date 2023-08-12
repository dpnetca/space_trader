from space_traders.models import ApiError, Meta


from math import ceil


def paginator(client, method, endpoint, limit=20, page=1, data=[], **kwargs):
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
