import pytest
from space_traders import SpaceTrader
from space_traders.models import (
    ConstructionCargo,
    ConstructionSite,
    Jumpgate,
    Market,
    Shipyard,
    System,
    Waypoint,
)


class TestSystems:
    @pytest.mark.asyncio
    async def test_get_system(self, st: SpaceTrader):
        response = await st.system.get_system("system")
        expected = {
            "data": {
                "symbol": "string",
                "sectorSymbol": "string",
                "type": "NEUTRON_STAR",
                "x": 0,
                "y": 0,
                "waypoints": [
                    {
                        "symbol": "string",
                        "type": "PLANET",
                        "x": 0,
                        "y": 0,
                        "orbitals": [{"symbol": "string"}],
                        "orbits": "string",
                    }
                ],
                "factions": [{"symbol": "COSMIC"}],
            }
        }
        expected_response = System(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_list_all_systems(self, st: SpaceTrader):
        response = await st.system.list_all_systems()
        expected = {
            "data": [
                {
                    "symbol": "string",
                    "sectorSymbol": "string",
                    "type": "NEUTRON_STAR",
                    "x": 0,
                    "y": 0,
                    "waypoints": [
                        {
                            "symbol": "string",
                            "type": "PLANET",
                            "x": 0,
                            "y": 0,
                            "orbitals": [{"symbol": "string"}],
                            "orbits": "string",
                        }
                    ],
                    "factions": [{"symbol": "COSMIC"}],
                }
            ],
            "meta": {"total": 0, "page": 1, "limit": 10},
        }

        expected_response = [System(**x) for x in expected["data"]]
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_get_waypoint_without_system(self, st: SpaceTrader):
        response = await st.system.get_waypoint("waypoint")
        expected = {
            "data": {
                "symbol": "string",
                "type": "PLANET",
                "systemSymbol": "string",
                "x": 0,
                "y": 0,
                "orbitals": [{"symbol": "string"}],
                "orbits": "string",
                "faction": {"symbol": "COSMIC"},
                "traits": [
                    {
                        "symbol": "UNCHARTED",
                        "name": "string",
                        "description": "string",
                    }
                ],
                "modifiers": [
                    {
                        "symbol": "STRIPPED",
                        "name": "string",
                        "description": "string",
                    }
                ],
                "chart": {
                    "waypointSymbol": "string",
                    "submittedBy": "string",
                    "submittedOn": "2019-08-24T14:15:22Z",
                },
                "isUnderConstruction": True,
            }
        }
        expected_response = Waypoint(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_get_waypoint_with_system(self, st: SpaceTrader):
        response = await st.system.get_waypoint("waypoint", "system")
        expected = {
            "data": {
                "symbol": "string",
                "type": "PLANET",
                "systemSymbol": "string",
                "x": 0,
                "y": 0,
                "orbitals": [{"symbol": "string"}],
                "orbits": "string",
                "faction": {"symbol": "COSMIC"},
                "traits": [
                    {
                        "symbol": "UNCHARTED",
                        "name": "string",
                        "description": "string",
                    }
                ],
                "modifiers": [
                    {
                        "symbol": "STRIPPED",
                        "name": "string",
                        "description": "string",
                    }
                ],
                "chart": {
                    "waypointSymbol": "string",
                    "submittedBy": "string",
                    "submittedOn": "2019-08-24T14:15:22Z",
                },
                "isUnderConstruction": True,
            }
        }
        expected_response = Waypoint(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_list_all_waypoints(self, st: SpaceTrader):
        response = await st.system.list_all_waypoints("system")
        expected = {
            "data": [
                {
                    "symbol": "string",
                    "type": "PLANET",
                    "systemSymbol": "string",
                    "x": 0,
                    "y": 0,
                    "orbitals": [{"symbol": "string"}],
                    "orbits": "string",
                    "faction": {"symbol": "COSMIC"},
                    "traits": [
                        {
                            "symbol": "UNCHARTED",
                            "name": "string",
                            "description": "string",
                        }
                    ],
                    "modifiers": [
                        {
                            "symbol": "STRIPPED",
                            "name": "string",
                            "description": "string",
                        }
                    ],
                    "chart": {
                        "waypointSymbol": "string",
                        "submittedBy": "string",
                        "submittedOn": "2019-08-24T14:15:22Z",
                    },
                    "isUnderConstruction": True,
                }
            ],
            "meta": {"total": 0, "page": 1, "limit": 10},
        }
        expected_response = [Waypoint(**x) for x in expected["data"]]
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_get_market_without_system(self, st: SpaceTrader):
        response = await st.system.get_market("waypoint")
        expected = {
            "data": {
                "symbol": "string",
                "exports": [
                    {
                        "symbol": "PRECIOUS_STONES",
                        "name": "string",
                        "description": "string",
                    }
                ],
                "imports": [
                    {
                        "symbol": "PRECIOUS_STONES",
                        "name": "string",
                        "description": "string",
                    }
                ],
                "exchange": [
                    {
                        "symbol": "PRECIOUS_STONES",
                        "name": "string",
                        "description": "string",
                    }
                ],
                "transactions": [
                    {
                        "waypointSymbol": "string",
                        "shipSymbol": "string",
                        "tradeSymbol": "string",
                        "type": "PURCHASE",
                        "units": 0,
                        "pricePerUnit": 0,
                        "totalPrice": 0,
                        "timestamp": "2019-08-24T14:15:22Z",
                    }
                ],
                "tradeGoods": [
                    {
                        "symbol": "string",
                        "type": "EXPORT",
                        "tradeVolume": 1,
                        "supply": "SCARCE",
                        "activity": "WEAK",
                        "purchasePrice": 0,
                        "sellPrice": 0,
                    }
                ],
            }
        }
        expected_response = Market(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_get_market_with_system(self, st: SpaceTrader):
        response = await st.system.get_market("waypoint", "system")
        expected = {
            "data": {
                "symbol": "string",
                "exports": [
                    {
                        "symbol": "PRECIOUS_STONES",
                        "name": "string",
                        "description": "string",
                    }
                ],
                "imports": [
                    {
                        "symbol": "PRECIOUS_STONES",
                        "name": "string",
                        "description": "string",
                    }
                ],
                "exchange": [
                    {
                        "symbol": "PRECIOUS_STONES",
                        "name": "string",
                        "description": "string",
                    }
                ],
                "transactions": [
                    {
                        "waypointSymbol": "string",
                        "shipSymbol": "string",
                        "tradeSymbol": "string",
                        "type": "PURCHASE",
                        "units": 0,
                        "pricePerUnit": 0,
                        "totalPrice": 0,
                        "timestamp": "2019-08-24T14:15:22Z",
                    }
                ],
                "tradeGoods": [
                    {
                        "symbol": "string",
                        "type": "EXPORT",
                        "tradeVolume": 1,
                        "supply": "SCARCE",
                        "activity": "WEAK",
                        "purchasePrice": 0,
                        "sellPrice": 0,
                    }
                ],
            }
        }
        expected_response = Market(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_get_jumpgate_without_system(self, st: SpaceTrader):
        response = await st.system.get_jumpgate("waypoint")
        expected = {"data": {"connections": ["string"]}}
        expected_response = Jumpgate(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_get_jumpgate_with_system(self, st: SpaceTrader):
        response = await st.system.get_jumpgate("waypoint", "system")
        expected = {"data": {"connections": ["string"]}}
        expected_response = Jumpgate(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_get_shipyard_without_system(self, st: SpaceTrader):
        response = await st.system.get_shipyard("waypoint")
        expected = {
            "data": {
                "symbol": "string",
                "shipTypes": [{"type": "SHIP_PROBE"}],
                "transactions": [
                    {
                        "waypointSymbol": "string",
                        "shipSymbol": "string",
                        "price": 0,
                        "agentSymbol": "string",
                        "timestamp": "2019-08-24T14:15:22Z",
                    }
                ],
                "ships": [
                    {
                        "type": "SHIP_PROBE",
                        "name": "string",
                        "description": "string",
                        "supply": "SCARCE",
                        "activity": "WEAK",
                        "purchasePrice": 0,
                        "frame": {
                            "symbol": "FRAME_PROBE",
                            "name": "string",
                            "description": "string",
                            "condition": 0,
                            "moduleSlots": 0,
                            "mountingPoints": 0,
                            "fuelCapacity": 0,
                            "requirements": {
                                "power": 0,
                                "crew": 0,
                                "slots": 0,
                            },
                        },
                        "reactor": {
                            "symbol": "REACTOR_SOLAR_I",
                            "name": "string",
                            "description": "string",
                            "condition": 0,
                            "powerOutput": 1,
                            "requirements": {
                                "power": 0,
                                "crew": 0,
                                "slots": 0,
                            },
                        },
                        "engine": {
                            "symbol": "ENGINE_IMPULSE_DRIVE_I",
                            "name": "string",
                            "description": "string",
                            "condition": 0,
                            "speed": 1,
                            "requirements": {
                                "power": 0,
                                "crew": 0,
                                "slots": 0,
                            },
                        },
                        "modules": [
                            {
                                "symbol": "MODULE_MINERAL_PROCESSOR_I",
                                "capacity": 0,
                                "range": 0,
                                "name": "string",
                                "description": "string",
                                "requirements": {
                                    "power": 0,
                                    "crew": 0,
                                    "slots": 0,
                                },
                            }
                        ],
                        "mounts": [
                            {
                                "symbol": "MOUNT_GAS_SIPHON_I",
                                "name": "string",
                                "description": "string",
                                "strength": 0,
                                "deposits": ["QUARTZ_SAND"],
                                "requirements": {
                                    "power": 0,
                                    "crew": 0,
                                    "slots": 0,
                                },
                            }
                        ],
                        "crew": {"required": 0, "capacity": 0},
                    }
                ],
                "modificationsFee": 0,
            }
        }
        expected_response = Shipyard(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_get_shipyard_with_system(self, st: SpaceTrader):
        response = await st.system.get_shipyard("waypoint", "system")
        expected = {
            "data": {
                "symbol": "string",
                "shipTypes": [{"type": "SHIP_PROBE"}],
                "transactions": [
                    {
                        "waypointSymbol": "string",
                        "shipSymbol": "string",
                        "price": 0,
                        "agentSymbol": "string",
                        "timestamp": "2019-08-24T14:15:22Z",
                    }
                ],
                "ships": [
                    {
                        "type": "SHIP_PROBE",
                        "name": "string",
                        "description": "string",
                        "supply": "SCARCE",
                        "activity": "WEAK",
                        "purchasePrice": 0,
                        "frame": {
                            "symbol": "FRAME_PROBE",
                            "name": "string",
                            "description": "string",
                            "condition": 0,
                            "moduleSlots": 0,
                            "mountingPoints": 0,
                            "fuelCapacity": 0,
                            "requirements": {
                                "power": 0,
                                "crew": 0,
                                "slots": 0,
                            },
                        },
                        "reactor": {
                            "symbol": "REACTOR_SOLAR_I",
                            "name": "string",
                            "description": "string",
                            "condition": 0,
                            "powerOutput": 1,
                            "requirements": {
                                "power": 0,
                                "crew": 0,
                                "slots": 0,
                            },
                        },
                        "engine": {
                            "symbol": "ENGINE_IMPULSE_DRIVE_I",
                            "name": "string",
                            "description": "string",
                            "condition": 0,
                            "speed": 1,
                            "requirements": {
                                "power": 0,
                                "crew": 0,
                                "slots": 0,
                            },
                        },
                        "modules": [
                            {
                                "symbol": "MODULE_MINERAL_PROCESSOR_I",
                                "capacity": 0,
                                "range": 0,
                                "name": "string",
                                "description": "string",
                                "requirements": {
                                    "power": 0,
                                    "crew": 0,
                                    "slots": 0,
                                },
                            }
                        ],
                        "mounts": [
                            {
                                "symbol": "MOUNT_GAS_SIPHON_I",
                                "name": "string",
                                "description": "string",
                                "strength": 0,
                                "deposits": ["QUARTZ_SAND"],
                                "requirements": {
                                    "power": 0,
                                    "crew": 0,
                                    "slots": 0,
                                },
                            }
                        ],
                        "crew": {"required": 0, "capacity": 0},
                    }
                ],
                "modificationsFee": 0,
            }
        }
        expected_response = Shipyard(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_get_construction_site_without_system(self, st: SpaceTrader):
        response = await st.system.get_construction_site("waypoint")
        expected = {
            "data": {
                "symbol": "string",
                "materials": [
                    {
                        "tradeSymbol": "PRECIOUS_STONES",
                        "required": 0,
                        "fulfilled": 0,
                    }
                ],
                "isComplete": True,
            }
        }
        expected_response = ConstructionSite(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_get_construction_site_with_system(self, st: SpaceTrader):
        response = await st.system.get_construction_site("waypoint", "system")
        expected = {
            "data": {
                "symbol": "string",
                "materials": [
                    {
                        "tradeSymbol": "PRECIOUS_STONES",
                        "required": 0,
                        "fulfilled": 0,
                    }
                ],
                "isComplete": True,
            }
        }
        expected_response = ConstructionSite(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_supply_construction_site_without_system(
        self, st: SpaceTrader
    ):
        response = await st.system.supply_construction_site(
            "ship", "trade", 1, "waypoint"
        )
        expected = {
            "data": {
                "construction": {
                    "symbol": "string",
                    "materials": [
                        {
                            "tradeSymbol": "PRECIOUS_STONES",
                            "required": 0,
                            "fulfilled": 0,
                        }
                    ],
                    "isComplete": True,
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
        }
        expected_response = ConstructionCargo(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_supply_construction_site_with_system(self, st: SpaceTrader):
        response = await st.system.supply_construction_site(
            "ship", "trade", 1, "waypoint", "system"
        )
        expected = {
            "data": {
                "construction": {
                    "symbol": "string",
                    "materials": [
                        {
                            "tradeSymbol": "PRECIOUS_STONES",
                            "required": 0,
                            "fulfilled": 0,
                        }
                    ],
                    "isComplete": True,
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
        }
        expected_response = ConstructionCargo(**expected["data"])
        assert response == expected_response
