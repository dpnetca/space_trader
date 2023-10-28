import pytest
from space_traders import SpaceTrader
from space_traders.models import Agent


class TestAgent:
    @pytest.mark.asyncio
    async def test_get_my_agent(self, st: SpaceTrader):
        agent = await st.agent.get_my_agent()
        expected_agent = Agent(
            **{
                "accountId": "string",
                "symbol": "string",
                "headquarters": "string",
                "credits": -9223372036854776000,
                "startingFaction": "string",
                "shipCount": 0,
            }
        )
        assert agent == expected_agent

    @pytest.mark.asyncio
    async def test_get_agent(self, st: SpaceTrader):
        agent = await st.agent.get_agent("agent")
        expected_agent = Agent(
            **{
                "accountId": "string",
                "symbol": "string",
                "headquarters": "string",
                "credits": -9223372036854776000,
                "startingFaction": "string",
                "shipCount": 0,
            }
        )
        assert agent == expected_agent

    @pytest.mark.asyncio
    async def test_list_all_agent(self, st: SpaceTrader):
        agents = await st.agent.list_all_agents()
        expected_agents = [
            Agent(
                **{
                    "accountId": "string",
                    "symbol": "string",
                    "headquarters": "string",
                    "credits": -9223372036854776000,
                    "startingFaction": "string",
                    "shipCount": 0,
                }
            )
        ]
        assert agents == expected_agents
