import pytest
from space_traders import SpaceTrader
from space_traders.models import Agent


class TestAgent:
    @pytest.mark.asyncio
    async def test_get_my_agent(self, st: SpaceTrader):
        response = await st.agent.get_my_agent()
        expected = {
            "data": {
                "accountId": "string",
                "symbol": "string",
                "headquarters": "string",
                "credits": -9007199254740991,
                "startingFaction": "string",
                "shipCount": 0,
            }
        }
        expected_response = Agent(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_get_agent(self, st: SpaceTrader):
        response = await st.agent.get_agent("agent")
        expected = {
            "data": {
                "accountId": "string",
                "symbol": "string",
                "headquarters": "string",
                "credits": -9007199254740991,
                "startingFaction": "string",
                "shipCount": 0,
            }
        }
        expected_response = Agent(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_list_all_agent(self, st: SpaceTrader):
        response = await st.agent.list_all_agents()
        expected = {
            "data": [
                {
                    "accountId": "string",
                    "symbol": "string",
                    "headquarters": "string",
                    "credits": -9007199254740991,
                    "startingFaction": "string",
                    "shipCount": 0,
                }
            ]
        }
        expected_response = [Agent(**x) for x in expected["data"]]
        assert response == expected_response
