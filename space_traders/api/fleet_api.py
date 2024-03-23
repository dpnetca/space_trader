import json
from typing import List
import logging

from space_traders.client import Client
from space_traders.models import (
    AgentRepairTransaction,
    AgentScrapTransaction,
    AgentCargoTransaction,
    AgentFuelTransaction,
    AgentMountCargoTransaction,
    AgentShipTransaction,
    ApiError,
    ChartWaypoint,
    CargoCooldownProducedConsumed,
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
    ShipCargo,
    ShipCooldown,
    ShipMount,
    ShipNav,
    Survey,
)
from space_traders.utils import paginator

log = logging.getLogger("SpaceTrader")


class FleetApi:
    def __init__(self, client: Client) -> None:
        self.client = client
        self.base_endpoint = "/my/ships"

    async def create_chart(self, symbol: str) -> ChartWaypoint | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/chart"
        response = await self.client.send("post", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return ChartWaypoint(**response["data"])

    async def create_survey(self, symbol: str) -> CooldownSurveys | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/survey"
        response = await self.client.send("post", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return CooldownSurveys(**response["data"])

    async def dock_ship(self, symbol: str) -> ShipNav | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/dock"
        response = await self.client.send("post", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return ShipNav(**response["data"]["nav"])

    async def extract_resources(
        self, symbol: str
    ) -> CooldownExtractionCargoEvent | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/extract"
        response = await self.client.send("post", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return CooldownExtractionCargoEvent(**response["data"])

    async def extract_survey(
        self, symbol: str, survey: Survey | None = None
    ) -> CooldownExtractionCargoEvent | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/extract/survey"
        data = json.loads(survey.model_dump_json())
        response = await self.client.send("post", endpoint, data=data)
        if "error" in response.keys():
            return ApiError(**response)
        return CooldownExtractionCargoEvent(**response["data"])

    async def get_mounts(self, symbol: str) -> List[ShipMount] | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/mounts"
        response = await self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return [ShipMount(**m) for m in response["data"]]

    async def get_repair_ship(self, symbol: str) -> RepairTransaction:
        endpoint = self.base_endpoint + f"/{symbol}/repair"
        response = await self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return RepairTransaction(**response["data"]["transaction"])

    async def get_scrap_ship(self, symbol: str) -> ScrapTransaction:
        endpoint = self.base_endpoint + f"/{symbol}/scrap"
        response = await self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return ScrapTransaction(**response["data"]["transaction"])

    async def get_ship(self, symbol: str) -> Ship | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}"
        response = await self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return Ship(**response["data"])

    async def get_ship_cargo(self, symbol: str) -> ShipCargo | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/cargo"
        response = await self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return ShipCargo(**response["data"])

    async def get_ship_cooldown(
        self, symbol: str
    ) -> ShipCooldown | ApiError | dict:
        endpoint = self.base_endpoint + f"/{symbol}/cooldown"
        response = await self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        if "data" in response.keys():
            return ShipCooldown(**response["data"])
        return response

    async def get_ship_nav(self, symbol: str) -> ShipNav | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/nav"
        response = await self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return ShipNav(**response["data"])

    async def jettison_cargo(
        self, symbol: str, item_symbol: str, units: int
    ) -> ShipCargo | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/jettison"
        data = {"symbol": item_symbol, "units": units}
        response = await self.client.send("post", endpoint, data=data)
        if "error" in response.keys():
            return ApiError(**response)
        return ShipCargo(**response["data"]["cargo"])

    async def jump_ship(
        self, symbol: str, waypoint_symbol: str
    ) -> NavCooldownTransactionAgent | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/jump"
        data = {"waypointSymbol": waypoint_symbol}
        response = await self.client.send("post", endpoint, data=data)
        if "error" in response.keys():
            return ApiError(**response)
        return NavCooldownTransactionAgent(**response["data"])

    async def list_all_ships(self) -> List[Ship] | ApiError:
        response = await paginator(self.client, "get", self.base_endpoint)
        if isinstance(response, ApiError):
            return response
        return [Ship(**s) for s in response]

    async def navigate_ship(
        self, symbol: str, waypoint_symbol: str
    ) -> FuelNavEvent | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/navigate"
        data = {"waypointSymbol": waypoint_symbol}
        response = await self.client.send("post", endpoint, data=data)
        if "error" in response.keys():
            return ApiError(**response)
        return FuelNavEvent(**response["data"])

    async def negotiate_contract(self, symbol: str) -> Contract | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/negotiate/contract"
        response = await self.client.send("post", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return Contract(**response["data"]["contract"])

    async def install_mount(
        self, ship_symbol: str, mount_symbol: str
    ) -> AgentMountCargoTransaction | ApiError:
        endpoint = self.base_endpoint + f"/{ship_symbol}/mounts/install"
        data = {"symbol": mount_symbol}
        response = await self.client.send("post", endpoint, data=data)
        if "error" in response.keys():
            return ApiError(**response)
        return AgentMountCargoTransaction(**response["data"])

    async def orbit_ship(self, symbol: str) -> ShipNav | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/orbit"
        response = await self.client.send("post", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return ShipNav(**response["data"]["nav"])

    async def patch_ship_nav(
        self, symbol: str, flight_mode: str
    ) -> ShipNav | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/nav"
        data = {"flightMode": flight_mode}
        response = await self.client.send("patch", endpoint, data=data)
        if "error" in response.keys():
            return ApiError(**response)
        return ShipNav(**response["data"])

    async def purchase_cargo(
        self, symbol: str, item_symbol: str, units: int
    ) -> AgentCargoTransaction | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/purchase"
        data = {"symbol": item_symbol, "units": units}
        response = await self.client.send("post", endpoint, data=data)
        if "error" in response.keys():
            return ApiError(**response)
        return AgentCargoTransaction(**response["data"])

    async def purchase_ship(
        self, ship_type: str, waypoint_symbol: str
    ) -> AgentShipTransaction | ApiError:
        endpoint = self.base_endpoint
        data = {
            "shipType": ship_type,
            "waypointSymbol": waypoint_symbol,
        }
        response = await self.client.send("post", endpoint, data=data)
        if "error" in response.keys():
            return ApiError(**response)
        return AgentShipTransaction(**response["data"])

    async def refuel_ship(
        self,
        symbol: str,
        units: int | None = None,
        from_cargo: bool | None = None,
    ) -> AgentFuelTransaction | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/refuel"

        data = {}
        if units is not None:
            data["units"] = units
        if from_cargo is not None:
            data["fromCargo"] = from_cargo

        response = await self.client.send("post", endpoint, data=data)
        if "error" in response.keys():
            return ApiError(**response)
        return AgentFuelTransaction(**response["data"])

    async def remove_mount(
        self, symbol: str, mount_symbol: str
    ) -> AgentMountCargoTransaction | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/mounts/remove"
        data = {"symbol": mount_symbol}
        response = await self.client.send("post", endpoint, data=data)
        if "error" in response.keys():
            return ApiError(**response)
        return AgentMountCargoTransaction(**response["data"])

    async def sell_cargo(
        self, symbol: str, item_symbol: str, units: int
    ) -> AgentCargoTransaction | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/sell"
        data = {"symbol": item_symbol, "units": units}
        response = await self.client.send("post", endpoint, data=data)
        if "error" in response.keys():
            return ApiError(**response)
        return AgentCargoTransaction(**response["data"])

    async def scan_ships(self, symbol: str) -> CooldownShips | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/scan/ships"
        response = await self.client.send("post", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return CooldownShips(**response["data"])

    async def scan_systems(self, symbol: str) -> CooldownSystems | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/scan/systems"
        response = await self.client.send("post", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return CooldownSystems(**response["data"])

    async def scan_waypoints(
        self, symbol: str
    ) -> CooldownWaypoints | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/scan/waypoints"
        response = await self.client.send("post", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return CooldownWaypoints(**response["data"])

    async def siphon_resources(
        self, symbol: str
    ) -> CooldownSiphonCargoEvent | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/siphon"
        response = await self.client.send("post", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return CooldownSiphonCargoEvent(**response["data"])

    async def ship_refine(
        self, symbol: str, produce: str
    ) -> CargoCooldownProducedConsumed | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/refine"
        data = {"produce": produce}
        response = await self.client.send("post", endpoint, data=data)
        if "error" in response.keys():
            return ApiError(**response)
        return CargoCooldownProducedConsumed(**response["data"])

    async def transfer_cargo(
        self, symbol: str, trade_symbol: str, units: int, target_ship: str
    ) -> ShipCargo | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/transfer"
        data = {
            "tradeSymbol": trade_symbol,
            "units": units,
            "shipSymbol": target_ship,
        }
        response = await self.client.send("post", endpoint, data=data)
        if "error" in response.keys():
            return ApiError(**response)
        return ShipCargo(**response["data"]["cargo"])

    async def warp_ship(
        self, symbol: str, waypoint_symbol: str
    ) -> FuelNavEvent | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/warp"
        data = {"waypointSymbol": waypoint_symbol}
        response = await self.client.send("post", endpoint, data=data)
        if "error" in response.keys():
            return ApiError(**response)
        return FuelNavEvent(**response["data"])
