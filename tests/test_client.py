import pytest
from space_traders import SpaceTrader
from space_traders.models.status import Status


class TestClient:
    @pytest.mark.asyncio
    async def test_valid_get(self, st: SpaceTrader):
        response = await st.client._get(st.client.base_url)
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_invalid_get(self, st: SpaceTrader):
        response = await st.client._get(st.client.base_url + "/invalid")
        print(response.status_code)
        # stoplight mock returns 422, actual returns 404
        assert response.status_code == 404 or response.status_code == 422

    @pytest.mark.asyncio
    async def test_valid_send_get(self, st: SpaceTrader):
        response = await st.client.send("get", "", auth=False)
        assert isinstance(response, dict)

    # mock server does not respond the same as actual server...not really valid
    # @pytest.mark.asyncio
    # async def test_invalid_send_get(self, st: SpaceTrader):
    #     response = await st.client.send("get", "/invalid", auth=False)
    #     # expected_response = {
    #     #     "error": {
    #     #         "message": "This route does not exist. Did you send the correct method or path? Check your request for typos: GET /invalid",
    #     #         "code": 404,
    #     #         "data": {"method": "GET", "path": "/invalid"},
    #     #     }
    #     # }
    #     expected_response = {
    #         "name": "https://stoplight.io/prism/errors#UNPROCESSABLE_ENTITY",
    #         "status": 422,
    #         "detail": "Route not resolved, no path matched",
    #         "additional": {
    #             "workspaceSlug": "spacetraders",
    #             "projectSlug": "spacetraders",
    #             "url": "/invalid",
    #             "dynamic": False,
    #         },
    #     }
    #     assert response == expected_response
