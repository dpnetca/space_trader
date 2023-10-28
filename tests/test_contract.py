import pytest
from space_traders import SpaceTrader
from space_traders.models import AgentContract, ContractCargo, Contract


class TestContract:
    @pytest.mark.asyncio
    async def test_accept_contract(self, st: SpaceTrader):
        response = await st.contract.accept_contract("xxx")
        expected_response = AgentContract(
            **{
                "agent": {
                    "accountId": "string",
                    "symbol": "string",
                    "headquarters": "string",
                    "credits": -9223372036854776000,
                    "startingFaction": "string",
                    "shipCount": 0,
                },
                "contract": {
                    "id": "string",
                    "factionSymbol": "string",
                    "type": "PROCUREMENT",
                    "terms": {
                        "deadline": "2019-08-24T14:15:22Z",
                        "payment": {"onAccepted": 0, "onFulfilled": 0},
                        "deliver": [
                            {
                                "tradeSymbol": "string",
                                "destinationSymbol": "string",
                                "unitsRequired": 0,
                                "unitsFulfilled": 0,
                            }
                        ],
                    },
                    "accepted": False,
                    "fulfilled": False,
                    "expiration": "2019-08-24T14:15:22Z",
                    "deadlineToAccept": "2019-08-24T14:15:22Z",
                },
            }
        )
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_deliver_cargo_to_contract(self, st: SpaceTrader):
        response = await st.contract.deliver_cargo_to_contract(
            "c_id", "s_id", "i_id", 12
        )
        expected_response = ContractCargo(
            **{
                "contract": {
                    "id": "string",
                    "factionSymbol": "string",
                    "type": "PROCUREMENT",
                    "terms": {
                        "deadline": "2019-08-24T14:15:22Z",
                        "payment": {"onAccepted": 0, "onFulfilled": 0},
                        "deliver": [
                            {
                                "tradeSymbol": "string",
                                "destinationSymbol": "string",
                                "unitsRequired": 0,
                                "unitsFulfilled": 0,
                            }
                        ],
                    },
                    "accepted": False,
                    "fulfilled": False,
                    "expiration": "2019-08-24T14:15:22Z",
                    "deadlineToAccept": "2019-08-24T14:15:22Z",
                },
                "cargo": {
                    "capacity": 0,
                    "units": 0,
                    "inventory": [
                        {
                            "symbol": "string",
                            "name": "string",
                            "description": "string",
                            "units": 1,
                        }
                    ],
                },
            }
        )
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_fulfill_contract(self, st: SpaceTrader):
        response = await st.contract.fulfill_contract("c_id")
        expected_response = AgentContract(
            **{
                "agent": {
                    "accountId": "string",
                    "symbol": "string",
                    "headquarters": "string",
                    "credits": -9223372036854776000,
                    "startingFaction": "string",
                    "shipCount": 0,
                },
                "contract": {
                    "id": "string",
                    "factionSymbol": "string",
                    "type": "PROCUREMENT",
                    "terms": {
                        "deadline": "2019-08-24T14:15:22Z",
                        "payment": {"onAccepted": 0, "onFulfilled": 0},
                        "deliver": [
                            {
                                "tradeSymbol": "string",
                                "destinationSymbol": "string",
                                "unitsRequired": 0,
                                "unitsFulfilled": 0,
                            }
                        ],
                    },
                    "accepted": False,
                    "fulfilled": False,
                    "expiration": "2019-08-24T14:15:22Z",
                    "deadlineToAccept": "2019-08-24T14:15:22Z",
                },
            }
        )
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_get_contract(self, st: SpaceTrader):
        response = await st.contract.get_contract("c_id")
        expected_response = Contract(
            **{
                "id": "string",
                "factionSymbol": "string",
                "type": "PROCUREMENT",
                "terms": {
                    "deadline": "2019-08-24T14:15:22Z",
                    "payment": {"onAccepted": 0, "onFulfilled": 0},
                    "deliver": [
                        {
                            "tradeSymbol": "string",
                            "destinationSymbol": "string",
                            "unitsRequired": 0,
                            "unitsFulfilled": 0,
                        }
                    ],
                },
                "accepted": False,
                "fulfilled": False,
                "expiration": "2019-08-24T14:15:22Z",
                "deadlineToAccept": "2019-08-24T14:15:22Z",
            }
        )
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_list_all_contract(self, st: SpaceTrader):
        response = await st.contract.list_all_contracts()
        expected_response = [
            Contract(
                **{
                    "id": "string",
                    "factionSymbol": "string",
                    "type": "PROCUREMENT",
                    "terms": {
                        "deadline": "2019-08-24T14:15:22Z",
                        "payment": {"onAccepted": 0, "onFulfilled": 0},
                        "deliver": [
                            {
                                "tradeSymbol": "string",
                                "destinationSymbol": "string",
                                "unitsRequired": 0,
                                "unitsFulfilled": 0,
                            }
                        ],
                    },
                    "accepted": False,
                    "fulfilled": False,
                    "expiration": "2019-08-24T14:15:22Z",
                    "deadlineToAccept": "2019-08-24T14:15:22Z",
                }
            )
        ]
        assert response == expected_response
