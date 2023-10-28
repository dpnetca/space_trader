import asyncio

import pytest

from space_traders import SpaceTrader


pytest_plugins = ("pytest_asyncio",)


@pytest.fixture()
def st():
    st_client = SpaceTrader(None)
    st_client.client.base_url = (
        "https://stoplight.io/mocks/spacetraders/spacetraders/96627693"
    )
    yield st_client
    asyncio.run(st_client.client.close())
