import pytest
from space_traders import SpaceTrader
from space_traders.models import (
    AgentCargoTransaction,
    AgentFuelTransaction,
    AgentMountCargoTransaction,
    AgentShipTransaction,
    AgentShipRepairTransaction,
    CargoCooldownProducedConsumed,
    ChartWaypoint,
    Contract,
    CooldownExtractionCargoEvent,
    CooldownSiphonCargoEvent,
    CooldownShips,
    CooldownSurveys,
    CooldownSystems,
    CooldownWaypoints,
    FuelNavEvent,
    NavCooldownTransactionAgent,
    RepairTransaction,
    ScrapTransaction,
    Ship,
    ShipCooldown,
    ShipCargo,
    ShipMount,
    ShipNav,
    Survey,
)


class TestFleet:
    @pytest.mark.asyncio
    async def test_create_chart(self, st: SpaceTrader):
        response = await st.fleet.create_chart("ship")
        expected = {
            "data": {
                "chart": {
                    "waypointSymbol": "string",
                    "submittedBy": "string",
                    "submittedOn": "2019-08-24T14:15:22Z",
                },
                "waypoint": {
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
                },
            }
        }
        expected_response = ChartWaypoint(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_create_survey(self, st: SpaceTrader):
        response = await st.fleet.create_survey("ship")
        expected = {
            "data": {
                "cooldown": {
                    "shipSymbol": "string",
                    "totalSeconds": 0,
                    "remainingSeconds": 0,
                    "expiration": "2019-08-24T14:15:22Z",
                },
                "surveys": [
                    {
                        "signature": "string",
                        "symbol": "string",
                        "deposits": [{"symbol": "string"}],
                        "expiration": "2019-08-24T14:15:22Z",
                        "size": "SMALL",
                    }
                ],
            }
        }
        expected_response = CooldownSurveys(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_dock_ship(self, st: SpaceTrader):
        response = await st.fleet.dock_ship("ship")
        expected = {
            "data": {
                "nav": {
                    "systemSymbol": "string",
                    "waypointSymbol": "string",
                    "route": {
                        "destination": {
                            "symbol": "string",
                            "type": "PLANET",
                            "systemSymbol": "string",
                            "x": 0,
                            "y": 0,
                        },
                        "origin": {
                            "symbol": "string",
                            "type": "PLANET",
                            "systemSymbol": "string",
                            "x": 0,
                            "y": 0,
                        },
                        "departureTime": "2019-08-24T14:15:22Z",
                        "arrival": "2019-08-24T14:15:22Z",
                    },
                    "status": "IN_TRANSIT",
                    "flightMode": "CRUISE",
                }
            }
        }
        expected_response = ShipNav(**expected["data"]["nav"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_extract_resources(self, st: SpaceTrader):
        response = await st.fleet.extract_resources("ship")
        expected = {
            "data": {
                "cooldown": {
                    "shipSymbol": "string",
                    "totalSeconds": 0,
                    "remainingSeconds": 0,
                    "expiration": "2019-08-24T14:15:22Z"
                },
                "extraction": {
                    "shipSymbol": "string",
                    "yield": {
                        "symbol": "PRECIOUS_STONES",
                        "units": 0
                    }
                },
                "cargo": {
                    "capacity": 0,
                    "units": 0,
                    "inventory": [
                        {
                            "symbol": "PRECIOUS_STONES",
                            "name": "string",
                            "description": "string",
                            "units": 1
                        }
                    ]
                },
                "events": [
                    {
                        "symbol": "REACTOR_OVERLOAD",
                        "component": "FRAME",
                        "name": "string",
                        "description": "string"
                    }
                ]
            }
        }
        expected_response = CooldownExtractionCargoEvent(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_extract_surveys(self, st: SpaceTrader):
        survey = Survey(
            **{
                "signature": "string",
                "symbol": "string",
                "deposits": [{"symbol": "string"}],
                "expiration": "2019-08-24T14:15:22Z",
                "size": "SMALL",
            }
        )
        response = await st.fleet.extract_survey("ship", survey)
        expected = {
            "data": {
                "cooldown": {
                    "shipSymbol": "string",
                    "totalSeconds": 0,
                    "remainingSeconds": 0,
                    "expiration": "2019-08-24T14:15:22Z"
                },
                "extraction": {
                    "shipSymbol": "string",
                    "yield": {
                        "symbol": "PRECIOUS_STONES",
                        "units": 0
                    }
                },
                "cargo": {
                    "capacity": 0,
                    "units": 0,
                    "inventory": [
                        {
                            "symbol": "PRECIOUS_STONES",
                            "name": "string",
                            "description": "string",
                            "units": 1
                        }
                    ]
                },
                "events": [
                    {
                        "symbol": "REACTOR_OVERLOAD",
                        "component": "FRAME",
                        "name": "string",
                        "description": "string"
                    }
                ]
            }
        }
        expected_response = CooldownExtractionCargoEvent(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_get_mounts(self, st: SpaceTrader):
        response = await st.fleet.get_mounts("ship")
        expected = {
            "data": [
                {
                    "symbol": "MOUNT_GAS_SIPHON_I",
                    "name": "string",
                    "description": "string",
                    "strength": 0,
                    "deposits": ["QUARTZ_SAND"],
                    "requirements": {"power": 0, "crew": 0, "slots": 0},
                }
            ]
        }
        expected_response = [ShipMount(**x) for x in expected["data"]]
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_get_scrap_ship(self, st: SpaceTrader):
        response = await st.fleet.get_scrap_ship("ship")
        expected = {
            "data": {
                "transaction": {
                    "waypointSymbol": "string",
                    "shipSymbol": "string",
                    "totalPrice": 0,
                    "timestamp": "2019-08-24T14:15:22Z"
                }
            }
        }
        expected_response = ScrapTransaction(**expected["data"]["transaction"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_get_repair_ship(self, st: SpaceTrader):
        response = await st.fleet.get_repair_ship("ship")
        expected = {
            "data": {
                "transaction": {
                    "waypointSymbol": "string",
                    "shipSymbol": "string",
                    "totalPrice": 0,
                    "timestamp": "2019-08-24T14:15:22Z"
                }
            }
        }
        expected_response = RepairTransaction(
            **expected["data"]["transaction"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_get_ship(self, st: SpaceTrader):
        response = await st.fleet.get_ship("ship")
        expected = {
            "data": {
                "symbol": "string",
                "registration": {
                    "name": "string",
                    "factionSymbol": "string",
                    "role": "FABRICATOR"
                },
                "nav": {
                    "systemSymbol": "string",
                    "waypointSymbol": "string",
                    "route": {
                        "destination": {
                            "symbol": "string",
                            "type": "PLANET",
                            "systemSymbol": "string",
                            "x": 0,
                            "y": 0
                        },
                        "origin": {
                            "symbol": "string",
                            "type": "PLANET",
                            "systemSymbol": "string",
                            "x": 0,
                            "y": 0
                        },
                        "departureTime": "2019-08-24T14:15:22Z",
                        "arrival": "2019-08-24T14:15:22Z"
                    },
                    "status": "IN_TRANSIT",
                    "flightMode": "CRUISE"
                },
                "crew": {
                    "current": 0,
                    "required": 0,
                    "capacity": 0,
                    "rotation": "STRICT",
                    "morale": 0,
                    "wages": 0
                },
                "frame": {
                    "symbol": "FRAME_PROBE",
                    "name": "string",
                    "description": "string",
                    "condition": 0,
                    "integrity": 0,
                    "moduleSlots": 0,
                    "mountingPoints": 0,
                    "fuelCapacity": 0,
                    "requirements": {
                        "power": 0,
                        "crew": 0,
                        "slots": 0
                    }
                },
                "reactor": {
                    "symbol": "REACTOR_SOLAR_I",
                    "name": "string",
                    "description": "string",
                    "condition": 0,
                    "integrity": 0,
                    "powerOutput": 1,
                    "requirements": {
                        "power": 0,
                        "crew": 0,
                        "slots": 0
                    }
                },
                "engine": {
                    "symbol": "ENGINE_IMPULSE_DRIVE_I",
                    "name": "string",
                    "description": "string",
                    "condition": 0,
                    "integrity": 0,
                    "speed": 1,
                    "requirements": {
                        "power": 0,
                        "crew": 0,
                        "slots": 0
                    }
                },
                "cooldown": {
                    "shipSymbol": "string",
                    "totalSeconds": 0,
                    "remainingSeconds": 0,
                    "expiration": "2019-08-24T14:15:22Z"
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
                            "slots": 0
                        }
                    }
                ],
                "mounts": [
                    {
                        "symbol": "MOUNT_GAS_SIPHON_I",
                        "name": "string",
                        "description": "string",
                        "strength": 0,
                        "deposits": [
                            "QUARTZ_SAND"
                        ],
                        "requirements": {
                            "power": 0,
                            "crew": 0,
                            "slots": 0
                        }
                    }
                ],
                "cargo": {
                    "capacity": 0,
                    "units": 0,
                    "inventory": [
                        {
                            "symbol": "PRECIOUS_STONES",
                            "name": "string",
                            "description": "string",
                            "units": 1
                        }
                    ]
                },
                "fuel": {
                    "current": 0,
                    "capacity": 0,
                    "consumed": {
                        "amount": 0,
                        "timestamp": "2019-08-24T14:15:22Z"
                    }
                }
            }
        }
        expected_response = Ship(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_get_ship_cargo(self, st: SpaceTrader):
        response = await st.fleet.get_ship_cargo("ship")
        expected = {
            "data": {
                "capacity": 0,
                "units": 0,
                "inventory": [
                    {
                        "symbol": "PRECIOUS_STONES",
                        "name": "string",
                        "description": "string",
                        "units": 1,
                    }
                ],
            }
        }
        expected_response = ShipCargo(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_get_ship_cooldown(self, st: SpaceTrader):
        response = await st.fleet.get_ship_cooldown("ship")
        expected = {
            "data": {
                "shipSymbol": "string",
                "totalSeconds": 0,
                "remainingSeconds": 0,
                "expiration": "2019-08-24T14:15:22Z",
            }
        }
        expected_response = ShipCooldown(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_get_ship_nav(self, st: SpaceTrader):
        response = await st.fleet.get_ship_nav("ship")
        expected = {
            "data": {
                "systemSymbol": "string",
                "waypointSymbol": "string",
                "route": {
                    "destination": {
                        "symbol": "string",
                        "type": "PLANET",
                        "systemSymbol": "string",
                        "x": 0,
                        "y": 0,
                    },
                    "origin": {
                        "symbol": "string",
                        "type": "PLANET",
                        "systemSymbol": "string",
                        "x": 0,
                        "y": 0,
                    },
                    "departureTime": "2019-08-24T14:15:22Z",
                    "arrival": "2019-08-24T14:15:22Z",
                },
                "status": "IN_TRANSIT",
                "flightMode": "CRUISE",
            }
        }
        expected_response = ShipNav(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_install_mount(self, st: SpaceTrader):
        response = await st.fleet.install_mount("ship", "MOUNT_MINING_LASER_I")
        expected = {
            "data": {
                "agent": {
                    "accountId": "string",
                    "symbol": "string",
                    "headquarters": "string",
                    "credits": -9007199254740991,
                    "startingFaction": "string",
                    "shipCount": 0,
                },
                "mounts": [
                    {
                        "symbol": "MOUNT_GAS_SIPHON_I",
                        "name": "string",
                        "description": "string",
                        "strength": 0,
                        "deposits": ["QUARTZ_SAND"],
                        "requirements": {"power": 0, "crew": 0, "slots": 0},
                    }
                ],
                "cargo": {
                    "capacity": 0,
                    "units": 0,
                    "inventory": [
                        {
                            "symbol": "PRECIOUS_STONES",
                            "name": "string",
                            "description": "string",
                            "units": 1,
                        }
                    ],
                },
                "transaction": {
                    "waypointSymbol": "string",
                    "shipSymbol": "string",
                    "tradeSymbol": "string",
                    "totalPrice": 0,
                    "timestamp": "2019-08-24T14:15:22Z",
                },
            }
        }
        expected_response = AgentMountCargoTransaction(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_jettison_cargo(self, st: SpaceTrader):
        response = await st.fleet.jettison_cargo("ship", "PRECIOUS_STONES", 1)
        expected = {
            "data": {
                "cargo": {
                    "capacity": 0,
                    "units": 0,
                    "inventory": [
                        {
                            "symbol": "PRECIOUS_STONES",
                            "name": "string",
                            "description": "string",
                            "units": 1,
                        }
                    ],
                }
            }
        }
        expected_response = ShipCargo(**expected["data"]["cargo"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_jump_ship(self, st: SpaceTrader):
        response = await st.fleet.jump_ship("ship", "waypoint")
        expected = {
            "data": {
                "nav": {
                    "systemSymbol": "string",
                    "waypointSymbol": "string",
                    "route": {
                        "destination": {
                            "symbol": "string",
                            "type": "PLANET",
                            "systemSymbol": "string",
                            "x": 0,
                            "y": 0,
                        },
                        "origin": {
                            "symbol": "string",
                            "type": "PLANET",
                            "systemSymbol": "string",
                            "x": 0,
                            "y": 0,
                        },
                        "departureTime": "2019-08-24T14:15:22Z",
                        "arrival": "2019-08-24T14:15:22Z",
                    },
                    "status": "IN_TRANSIT",
                    "flightMode": "CRUISE",
                },
                "cooldown": {
                    "shipSymbol": "string",
                    "totalSeconds": 0,
                    "remainingSeconds": 0,
                    "expiration": "2019-08-24T14:15:22Z",
                },
                "transaction": {
                    "waypointSymbol": "string",
                    "shipSymbol": "string",
                    "tradeSymbol": "string",
                    "type": "PURCHASE",
                    "units": 0,
                    "pricePerUnit": 0,
                    "totalPrice": 0,
                    "timestamp": "2019-08-24T14:15:22Z",
                },
                "agent": {
                    "accountId": "string",
                    "symbol": "string",
                    "headquarters": "string",
                    "credits": -9007199254740991,
                    "startingFaction": "string",
                    "shipCount": 0,
                },
            }
        }
        expected_response = NavCooldownTransactionAgent(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_list_all_ships(self, st: SpaceTrader):
        response = await st.fleet.list_all_ships()
        expected = {
            "data": [
                {
                    "symbol": "string",
                    "registration": {
                        "name": "string",
                                "factionSymbol": "string",
                                "role": "FABRICATOR"
                    },
                    "nav": {
                        "systemSymbol": "string",
                        "waypointSymbol": "string",
                        "route": {
                                        "destination": {
                                            "symbol": "string",
                                            "type": "PLANET",
                                            "systemSymbol": "string",
                                            "x": 0,
                                            "y": 0
                                        },
                            "origin": {
                                            "symbol": "string",
                                            "type": "PLANET",
                                            "systemSymbol": "string",
                                            "x": 0,
                                            "y": 0
                                        },
                            "departureTime": "2019-08-24T14:15:22Z",
                            "arrival": "2019-08-24T14:15:22Z"
                        },
                        "status": "IN_TRANSIT",
                        "flightMode": "CRUISE"
                    },
                    "crew": {
                        "current": 0,
                        "required": 0,
                        "capacity": 0,
                        "rotation": "STRICT",
                                    "morale": 0,
                                    "wages": 0
                    },
                    "frame": {
                        "symbol": "FRAME_PROBE",
                        "name": "string",
                        "description": "string",
                        "condition": 0,
                        "integrity": 0,
                        "moduleSlots": 0,
                        "mountingPoints": 0,
                        "fuelCapacity": 0,
                        "requirements": {
                            "power": 0,
                            "crew": 0,
                            "slots": 0
                        }
                    },
                    "reactor": {
                        "symbol": "REACTOR_SOLAR_I",
                        "name": "string",
                        "description": "string",
                        "condition": 0,
                        "integrity": 0,
                        "powerOutput": 1,
                        "requirements": {
                            "power": 0,
                            "crew": 0,
                            "slots": 0
                        }
                    },
                    "engine": {
                        "symbol": "ENGINE_IMPULSE_DRIVE_I",
                        "name": "string",
                        "description": "string",
                        "condition": 0,
                        "integrity": 0,
                        "speed": 1,
                        "requirements": {
                            "power": 0,
                            "crew": 0,
                            "slots": 0
                        }
                    },
                    "cooldown": {
                        "shipSymbol": "string",
                        "totalSeconds": 0,
                        "remainingSeconds": 0,
                        "expiration": "2019-08-24T14:15:22Z"
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
                                "slots": 0
                            }
                        }
                    ],
                    "mounts": [
                        {
                            "symbol": "MOUNT_GAS_SIPHON_I",
                            "name": "string",
                                    "description": "string",
                                    "strength": 0,
                            "deposits": [
                                "QUARTZ_SAND"
                            ],
                            "requirements": {
                                "power": 0,
                                "crew": 0,
                                "slots": 0
                            }
                        }
                    ],
                    "cargo": {
                        "capacity": 0,
                        "units": 0,
                        "inventory": [
                            {
                                "symbol": "PRECIOUS_STONES",
                                "name": "string",
                                        "description": "string",
                                "units": 1
                            }
                        ]
                    },
                    "fuel": {
                        "current": 0,
                        "capacity": 0,
                        "consumed": {
                            "amount": 0,
                            "timestamp": "2019-08-24T14:15:22Z"
                        }
                    }
                }
            ],
            "meta": {
                "total": 0,
                "page": 1,
                "limit": 10
            }
        }
        expected_response = [Ship(**x) for x in expected["data"]]
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_navigate_ship(self, st: SpaceTrader):
        response = await st.fleet.navigate_ship("ship", "waypoint")
        expected = {
            "data": {
                "fuel": {
                    "current": 0,
                    "capacity": 0,
                    "consumed": {
                        "amount": 0,
                        "timestamp": "2019-08-24T14:15:22Z"
                    }
                },
                "nav": {
                    "systemSymbol": "string",
                    "waypointSymbol": "string",
                    "route": {
                        "destination": {
                            "symbol": "string",
                            "type": "PLANET",
                            "systemSymbol": "string",
                                            "x": 0,
                            "y": 0
                        },
                        "origin": {
                            "symbol": "string",
                            "type": "PLANET",
                            "systemSymbol": "string",
                            "x": 0,
                            "y": 0
                        },
                        "departureTime": "2019-08-24T14:15:22Z",
                        "arrival": "2019-08-24T14:15:22Z"
                    },
                    "status": "IN_TRANSIT",
                    "flightMode": "CRUISE"
                },
                "events": [
                    {
                        "symbol": "REACTOR_OVERLOAD",
                        "component": "FRAME",
                        "name": "string",
                        "description": "string"
                    }
                ]
            }
        }
        expected_response = FuelNavEvent(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_negotiate_contract(self, st: SpaceTrader):
        response = await st.fleet.negotiate_contract("ship")
        expected = {
            "data": {
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
                }
            }
        }
        expected_response = Contract(**expected["data"]["contract"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_orbit_ship(self, st: SpaceTrader):
        response = await st.fleet.orbit_ship("ship")
        expected = {
            "data": {
                "nav": {
                    "systemSymbol": "string",
                    "waypointSymbol": "string",
                    "route": {
                        "destination": {
                            "symbol": "string",
                            "type": "PLANET",
                            "systemSymbol": "string",
                            "x": 0,
                            "y": 0,
                        },
                        "origin": {
                            "symbol": "string",
                            "type": "PLANET",
                            "systemSymbol": "string",
                            "x": 0,
                            "y": 0,
                        },
                        "departureTime": "2019-08-24T14:15:22Z",
                        "arrival": "2019-08-24T14:15:22Z",
                    },
                    "status": "IN_TRANSIT",
                    "flightMode": "CRUISE",
                }
            }
        }
        expected_response = ShipNav(**expected["data"]["nav"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_patch_ship_nav(self, st: SpaceTrader):
        response = await st.fleet.patch_ship_nav("ship", "CRUISE")
        expected = {
            "data": {
                "systemSymbol": "string",
                "waypointSymbol": "string",
                "route": {
                    "destination": {
                        "symbol": "string",
                        "type": "PLANET",
                        "systemSymbol": "string",
                        "x": 0,
                        "y": 0,
                    },
                    "origin": {
                        "symbol": "string",
                        "type": "PLANET",
                        "systemSymbol": "string",
                        "x": 0,
                        "y": 0,
                    },
                    "departureTime": "2019-08-24T14:15:22Z",
                    "arrival": "2019-08-24T14:15:22Z",
                },
                "status": "IN_TRANSIT",
                "flightMode": "CRUISE",
            }
        }
        expected_response = ShipNav(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_purchase_cargo(self, st: SpaceTrader):
        response = await st.fleet.purchase_cargo("ship", "PRECIOUS_STONES", 1)
        expected = {
            "data": {
                "agent": {
                    "accountId": "string",
                    "symbol": "string",
                    "headquarters": "string",
                    "credits": -9007199254740991,
                    "startingFaction": "string",
                    "shipCount": 0,
                },
                "cargo": {
                    "capacity": 0,
                    "units": 0,
                    "inventory": [
                        {
                            "symbol": "PRECIOUS_STONES",
                            "name": "string",
                            "description": "string",
                            "units": 1,
                        }
                    ],
                },
                "transaction": {
                    "waypointSymbol": "string",
                    "shipSymbol": "string",
                    "tradeSymbol": "string",
                    "type": "PURCHASE",
                    "units": 0,
                    "pricePerUnit": 0,
                    "totalPrice": 0,
                    "timestamp": "2019-08-24T14:15:22Z",
                },
            }
        }
        expected_response = AgentCargoTransaction(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_purchase_ship(self, st: SpaceTrader):
        response = await st.fleet.purchase_ship("SHIP_PROBE", "waypoint")
        expected = {
            "data": {
                "agent": {
                    "accountId": "string",
                    "symbol": "string",
                    "headquarters": "string",
                    "credits": -9007199254740991,
                    "startingFaction": "string",
                    "shipCount": 0
                },
                "ship": {
                    "symbol": "string",
                    "registration": {
                        "name": "string",
                        "factionSymbol": "string",
                        "role": "FABRICATOR"
                    },
                    "nav": {
                        "systemSymbol": "string",
                        "waypointSymbol": "string",
                        "route": {
                            "destination": {
                                "symbol": "string",
                                "type": "PLANET",
                                "systemSymbol": "string",
                                                "x": 0,
                                "y": 0
                            },
                            "origin": {
                                "symbol": "string",
                                "type": "PLANET",
                                "systemSymbol": "string",
                                "x": 0,
                                "y": 0
                            },
                            "departureTime": "2019-08-24T14:15:22Z",
                            "arrival": "2019-08-24T14:15:22Z"
                        },
                        "status": "IN_TRANSIT",
                        "flightMode": "CRUISE"
                    },
                    "crew": {
                        "current": 0,
                        "required": 0,
                        "capacity": 0,
                        "rotation": "STRICT",
                        "morale": 0,
                        "wages": 0
                    },
                    "frame": {
                        "symbol": "FRAME_PROBE",
                        "name": "string",
                        "description": "string",
                        "condition": 0,
                        "integrity": 0,
                        "moduleSlots": 0,
                        "mountingPoints": 0,
                        "fuelCapacity": 0,
                        "requirements": {
                            "power": 0,
                            "crew": 0,
                            "slots": 0
                        }
                    },
                    "reactor": {
                        "symbol": "REACTOR_SOLAR_I",
                        "name": "string",
                        "description": "string",
                        "condition": 0,
                        "integrity": 0,
                        "powerOutput": 1,
                        "requirements": {
                            "power": 0,
                            "crew": 0,
                            "slots": 0
                        }
                    },
                    "engine": {
                        "symbol": "ENGINE_IMPULSE_DRIVE_I",
                        "name": "string",
                        "description": "string",
                        "condition": 0,
                        "integrity": 0,
                        "speed": 1,
                        "requirements": {
                            "power": 0,
                            "crew": 0,
                            "slots": 0
                        }
                    },
                    "cooldown": {
                        "shipSymbol": "string",
                        "totalSeconds": 0,
                        "remainingSeconds": 0,
                        "expiration": "2019-08-24T14:15:22Z"
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
                                "slots": 0
                            }
                        }
                    ],
                    "mounts": [
                        {
                            "symbol": "MOUNT_GAS_SIPHON_I",
                            "name": "string",
                                    "description": "string",
                            "strength": 0,
                            "deposits": [
                                "QUARTZ_SAND"
                            ],
                            "requirements": {
                                "power": 0,
                                "crew": 0,
                                "slots": 0
                            }
                        }
                    ],
                    "cargo": {
                        "capacity": 0,
                        "units": 0,
                        "inventory": [
                            {
                                "symbol": "PRECIOUS_STONES",
                                "name": "string",
                                "description": "string",
                                "units": 1
                            }
                        ]
                    },
                    "fuel": {
                        "current": 0,
                        "capacity": 0,
                        "consumed": {
                            "amount": 0,
                            "timestamp": "2019-08-24T14:15:22Z"
                        }
                    }
                },
                "transaction": {
                    "waypointSymbol": "string",
                    "shipSymbol": "string",
                    "shipType": "string",
                    "price": 0,
                    "agentSymbol": "string",
                    "timestamp": "2019-08-24T14:15:22Z"
                }
            }
        }
        expected_response = AgentShipTransaction(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_refuel_ship(self, st: SpaceTrader):
        response = await st.fleet.refuel_ship("ship")
        expected = {
            "data": {
                "agent": {
                    "accountId": "string",
                    "symbol": "string",
                    "headquarters": "string",
                    "credits": -9007199254740991,
                    "startingFaction": "string",
                    "shipCount": 0,
                },
                "fuel": {
                    "current": 0,
                    "capacity": 0,
                    "consumed": {
                        "amount": 0,
                        "timestamp": "2019-08-24T14:15:22Z",
                    },
                },
                "transaction": {
                    "waypointSymbol": "string",
                    "shipSymbol": "string",
                    "tradeSymbol": "string",
                    "type": "PURCHASE",
                    "units": 0,
                    "pricePerUnit": 0,
                    "totalPrice": 0,
                    "timestamp": "2019-08-24T14:15:22Z",
                },
            }
        }
        expected_response = AgentFuelTransaction(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_remove_mount(self, st: SpaceTrader):
        response = await st.fleet.remove_mount("ship", "MOUNT_MINING_LASER_I")
        expected = {
            "data": {
                "agent": {
                    "accountId": "string",
                    "symbol": "string",
                    "headquarters": "string",
                    "credits": -9007199254740991,
                    "startingFaction": "string",
                    "shipCount": 0,
                },
                "mounts": [
                    {
                        "symbol": "MOUNT_GAS_SIPHON_I",
                        "name": "string",
                        "description": "string",
                        "strength": 0,
                        "deposits": ["QUARTZ_SAND"],
                        "requirements": {"power": 0, "crew": 0, "slots": 0},
                    }
                ],
                "cargo": {
                    "capacity": 0,
                    "units": 0,
                    "inventory": [
                        {
                            "symbol": "PRECIOUS_STONES",
                            "name": "string",
                            "description": "string",
                            "units": 1,
                        }
                    ],
                },
                "transaction": {
                    "waypointSymbol": "string",
                    "shipSymbol": "string",
                    "tradeSymbol": "string",
                    "totalPrice": 0,
                    "timestamp": "2019-08-24T14:15:22Z",
                },
            }
        }
        expected_response = AgentMountCargoTransaction(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_repair_ship(self, st: SpaceTrader):
        response = await st.fleet.repair_ship("ship")
        expected = {
            "data": {
                "agent": {
                    "accountId": "string",
                    "symbol": "string",
                    "headquarters": "string",
                    "credits": -9007199254740991,
                    "startingFaction": "string",
                    "shipCount": 0
                },
                "ship": {
                    "symbol": "string",
                    "registration": {
                              "name": "string",
                              "factionSymbol": "string",
                              "role": "FABRICATOR"
                    },
                    "nav": {
                        "systemSymbol": "string",
                        "waypointSymbol": "string",
                        "route": {
                            "destination": {
                                "symbol": "string",
                                "type": "PLANET",
                                "systemSymbol": "string",
                                                "x": 0,
                                                "y": 0
                            },
                            "origin": {
                                "symbol": "string",
                                "type": "PLANET",
                                "systemSymbol": "string",
                                                "x": 0,
                                                "y": 0
                            },
                            "departureTime": "2019-08-24T14:15:22Z",
                            "arrival": "2019-08-24T14:15:22Z"
                        },
                        "status": "IN_TRANSIT",
                        "flightMode": "CRUISE"
                    },
                    "crew": {
                        "current": 0,
                        "required": 0,
                        "capacity": 0,
                        "rotation": "STRICT",
                        "morale": 0,
                        "wages": 0
                    },
                    "frame": {
                        "symbol": "FRAME_PROBE",
                        "name": "string",
                        "description": "string",
                        "condition": 0,
                        "integrity": 0,
                        "moduleSlots": 0,
                        "mountingPoints": 0,
                        "fuelCapacity": 0,
                        "requirements": {
                            "power": 0,
                            "crew": 0,
                            "slots": 0
                        }
                    },
                    "reactor": {
                        "symbol": "REACTOR_SOLAR_I",
                        "name": "string",
                        "description": "string",
                        "condition": 0,
                        "integrity": 0,
                        "powerOutput": 1,
                        "requirements": {
                            "power": 0,
                            "crew": 0,
                            "slots": 0
                        }
                    },
                    "engine": {
                        "symbol": "ENGINE_IMPULSE_DRIVE_I",
                        "name": "string",
                        "description": "string",
                        "condition": 0,
                        "integrity": 0,
                        "speed": 1,
                        "requirements": {
                            "power": 0,
                            "crew": 0,
                            "slots": 0
                        }
                    },
                    "cooldown": {
                        "shipSymbol": "string",
                        "totalSeconds": 0,
                        "remainingSeconds": 0,
                        "expiration": "2019-08-24T14:15:22Z"
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
                                      "slots": 0
                            }
                        }
                    ],
                    "mounts": [
                        {
                            "symbol": "MOUNT_GAS_SIPHON_I",
                            "name": "string",
                            "description": "string",
                            "strength": 0,
                            "deposits": [
                                      "QUARTZ_SAND"
                            ],
                            "requirements": {
                                "power": 0,
                                "crew": 0,
                                "slots": 0
                            }
                        }
                    ],
                    "cargo": {
                        "capacity": 0,
                        "units": 0,
                        "inventory": [
                            {
                                "symbol": "PRECIOUS_STONES",
                                "name": "string",
                                "description": "string",
                                "units": 1
                            }
                        ]
                    },
                    "fuel": {
                        "current": 0,
                        "capacity": 0,
                        "consumed": {
                            "amount": 0,
                            "timestamp": "2019-08-24T14:15:22Z"
                        }
                    }
                },
                "transaction": {
                    "waypointSymbol": "string",
                    "shipSymbol": "string",
                    "totalPrice": 0,
                    "timestamp": "2019-08-24T14:15:22Z"
                }
            }
        }
        expected_response = AgentShipRepairTransaction(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_scan_ships(self, st: SpaceTrader):
        response = await st.fleet.scan_ships("ship")
        expected = {
            "data": {
                "cooldown": {
                    "shipSymbol": "string",
                    "totalSeconds": 0,
                    "remainingSeconds": 0,
                    "expiration": "2019-08-24T14:15:22Z",
                },
                "ships": [
                    {
                        "symbol": "string",
                        "registration": {
                            "name": "string",
                            "factionSymbol": "string",
                            "role": "FABRICATOR",
                        },
                        "nav": {
                            "systemSymbol": "string",
                            "waypointSymbol": "string",
                            "route": {
                                "destination": {
                                    "symbol": "string",
                                    "type": "PLANET",
                                    "systemSymbol": "string",
                                    "x": 0,
                                    "y": 0,
                                },
                                "origin": {
                                    "symbol": "string",
                                    "type": "PLANET",
                                    "systemSymbol": "string",
                                    "x": 0,
                                    "y": 0,
                                },
                                "departureTime": "2019-08-24T14:15:22Z",
                                "arrival": "2019-08-24T14:15:22Z",
                            },
                            "status": "IN_TRANSIT",
                            "flightMode": "CRUISE",
                        },
                        "frame": {"symbol": "string"},
                        "reactor": {"symbol": "string"},
                        "engine": {"symbol": "string"},
                        "mounts": [{"symbol": "string"}],
                    }
                ],
            }
        }
        expected_response = CooldownShips(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_scan_systems(self, st: SpaceTrader):
        response = await st.fleet.scan_systems("ship")
        expected = {
            "data": {
                "cooldown": {
                    "shipSymbol": "string",
                    "totalSeconds": 0,
                    "remainingSeconds": 0,
                    "expiration": "2019-08-24T14:15:22Z",
                },
                "systems": [
                    {
                        "symbol": "string",
                        "sectorSymbol": "string",
                        "type": "NEUTRON_STAR",
                        "x": 0,
                        "y": 0,
                        "distance": 0,
                    }
                ],
            }
        }
        expected_response = CooldownSystems(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_scan_waypoints(self, st: SpaceTrader):
        response = await st.fleet.scan_waypoints("ship")
        expected = {
            "data": {
                "cooldown": {
                    "shipSymbol": "string",
                    "totalSeconds": 0,
                    "remainingSeconds": 0,
                    "expiration": "2019-08-24T14:15:22Z",
                },
                "waypoints": [
                    {
                        "symbol": "string",
                        "type": "PLANET",
                        "systemSymbol": "string",
                        "x": 0,
                        "y": 0,
                        "orbitals": [{"symbol": "string"}],
                        "faction": {"symbol": "COSMIC"},
                        "traits": [
                            {
                                "symbol": "UNCHARTED",
                                "name": "string",
                                "description": "string",
                            }
                        ],
                        "chart": {
                            "waypointSymbol": "string",
                            "submittedBy": "string",
                            "submittedOn": "2019-08-24T14:15:22Z",
                        },
                    }
                ],
            }
        }
        expected_response = CooldownWaypoints(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_sell_cargo(self, st: SpaceTrader):
        response = await st.fleet.sell_cargo("ship", "PRECIOUS_STONES", 1)
        expected = {
            "data": {
                "agent": {
                    "accountId": "string",
                    "symbol": "string",
                    "headquarters": "string",
                    "credits": -9007199254740991,
                    "startingFaction": "string",
                    "shipCount": 0,
                },
                "cargo": {
                    "capacity": 0,
                    "units": 0,
                    "inventory": [
                        {
                            "symbol": "PRECIOUS_STONES",
                            "name": "string",
                            "description": "string",
                            "units": 1,
                        }
                    ],
                },
                "transaction": {
                    "waypointSymbol": "string",
                    "shipSymbol": "string",
                    "tradeSymbol": "string",
                    "type": "PURCHASE",
                    "units": 0,
                    "pricePerUnit": 0,
                    "totalPrice": 0,
                    "timestamp": "2019-08-24T14:15:22Z",
                },
            }
        }
        expected_response = AgentCargoTransaction(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_ship_refine(self, st: SpaceTrader):
        response = await st.fleet.ship_refine("ship", "IRON")
        expected = {
            "data": {
                "cargo": {
                    "capacity": 0,
                    "units": 0,
                    "inventory": [
                        {
                            "symbol": "PRECIOUS_STONES",
                            "name": "string",
                            "description": "string",
                            "units": 1,
                        }
                    ],
                },
                "cooldown": {
                    "shipSymbol": "string",
                    "totalSeconds": 0,
                    "remainingSeconds": 0,
                    "expiration": "2019-08-24T14:15:22Z",
                },
                "produced": [{"tradeSymbol": "string", "units": 0}],
                "consumed": [{"tradeSymbol": "string", "units": 0}],
            }
        }
        expected_response = CargoCooldownProducedConsumed(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_siphon_resources(self, st: SpaceTrader):
        response = await st.fleet.siphon_resources("ship")
        expected = {
            "data": {
                "cooldown": {
                    "shipSymbol": "string",
                    "totalSeconds": 0,
                    "remainingSeconds": 0,
                    "expiration": "2019-08-24T14:15:22Z"
                },
                "siphon": {
                    "shipSymbol": "string",
                    "yield": {
                        "symbol": "PRECIOUS_STONES",
                        "units": 0
                    }
                },
                "cargo": {
                    "capacity": 0,
                    "units": 0,
                    "inventory": [
                        {
                            "symbol": "PRECIOUS_STONES",
                            "name": "string",
                            "description": "string",
                            "units": 1
                        }
                    ]
                },
                "events": [
                    {
                        "symbol": "REACTOR_OVERLOAD",
                        "component": "FRAME",
                        "name": "string",
                        "description": "string"
                    }
                ]
            }
        }
        expected_response = CooldownSiphonCargoEvent(**expected["data"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_transfer_cargo(self, st: SpaceTrader):
        response = await st.fleet.transfer_cargo(
            "ship", "PRECIOUS_STONES", 1, "target_ship"
        )
        expected = {
            "data": {
                "cargo": {
                    "capacity": 0,
                    "units": 0,
                    "inventory": [
                        {
                            "symbol": "PRECIOUS_STONES",
                            "name": "string",
                            "description": "string",
                            "units": 1,
                        }
                    ],
                }
            }
        }
        expected_response = ShipCargo(**expected["data"]["cargo"])
        assert response == expected_response

    @pytest.mark.asyncio
    async def test_warp_ship(self, st: SpaceTrader):
        response = await st.fleet.warp_ship("ship", "waypoint")
        expected = {
            "data": {
                "fuel": {
                    "current": 0,
                    "capacity": 0,
                    "consumed": {
                        "amount": 0,
                        "timestamp": "2019-08-24T14:15:22Z",
                    },
                },
                "nav": {
                    "systemSymbol": "string",
                    "waypointSymbol": "string",
                    "route": {
                        "destination": {
                            "symbol": "string",
                            "type": "PLANET",
                            "systemSymbol": "string",
                            "x": 0,
                            "y": 0,
                        },
                        "origin": {
                            "symbol": "string",
                            "type": "PLANET",
                            "systemSymbol": "string",
                            "x": 0,
                            "y": 0,
                        },
                        "departureTime": "2019-08-24T14:15:22Z",
                        "arrival": "2019-08-24T14:15:22Z",
                    },
                    "status": "IN_TRANSIT",
                    "flightMode": "CRUISE",
                },
            }
        }
        expected_response = FuelNavEvent(**expected["data"])
        assert response == expected_response
