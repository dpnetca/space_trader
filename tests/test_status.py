import pytest
from space_traders import SpaceTrader
from space_traders.models.status import Status


class TestStatus:
    @pytest.mark.asyncio
    async def test_get_status(self, st: SpaceTrader):
        status = await st.get_status()
        expected_status = Status(
            **{
                "status": "string",
                "version": "string",
                "resetDate": "string",
                "description": "string",
                "stats": {
                    "agents": 0,
                    "ships": 0,
                    "systems": 0,
                    "waypoints": 0,
                },
                "leaderboards": {
                    "mostCredits": [
                        {
                            "agentSymbol": "string",
                            "credits": -9223372036854776000,
                        }
                    ],
                    "mostSubmittedCharts": [
                        {"agentSymbol": "string", "chartCount": 0}
                    ],
                },
                "serverResets": {"next": "string", "frequency": "string"},
                "announcements": [{"title": "string", "body": "string"}],
                "links": [{"name": "string", "url": "string"}],
            }
        )
        assert status == expected_status
