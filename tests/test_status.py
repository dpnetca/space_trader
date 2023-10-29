import pytest
from space_traders import SpaceTrader
from space_traders.models.status import Status


class TestStatus:
    @pytest.mark.asyncio
    async def test_get_status(self, st: SpaceTrader):
        response = await st.get_status()
        expected = {
            "data": {
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
        }
        expected_response = Status(**expected["data"])
        assert response == expected_response
