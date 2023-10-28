import pytest
from space_traders import SpaceTrader
from space_traders.models import Faction


class TestFaction:
    @pytest.mark.asyncio
    async def test_get_faction(self, st: SpaceTrader):
        response = await st.faction.get_faction("COSMIC")
        expected = {
            "data": {
                "symbol": "COSMIC",
                "name": "string",
                "description": "string",
                "headquarters": "string",
                "traits": [
                    {
                        "symbol": "BUREAUCRATIC",
                        "name": "string",
                        "description": "string",
                    }
                ],
                "isRecruiting": True,
            }
        }
        expected_response = Faction(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_list_all_factions(self, st: SpaceTrader):
        response = await st.faction.list_all_factions()
        expected = {
            "data": [
                {
                    "symbol": "COSMIC",
                    "name": "string",
                    "description": "string",
                    "headquarters": "string",
                    "traits": [
                        {
                            "symbol": "BUREAUCRATIC",
                            "name": "string",
                            "description": "string",
                        }
                    ],
                    "isRecruiting": True,
                }
            ]
        }
        expected_response = [Faction(**x) for x in expected["data"]]
        assert response == expected_response
