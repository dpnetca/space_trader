import json
from typing import List

from space_traders.client import Client
from space_traders.models import (
    AgentCargoTransaction,
    AgentFuelTransaction,
    AgentShipTransaction,
    ApiError,
    CooldownExtractionCargo,
    CooldownSurveys,
    Ship,
    ShipCargo,
    ShipCooldown,
    ShipNav,
    Survey,
)
from space_traders.utils import paginator


class ShipApi:
    def __init__(self, client: Client) -> None:
        self.client = client
        self.base_endpoint = "/my/ships"

    def cargo(self, symbol: str) -> ShipCargo | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/cargo"
        response = self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return ShipCargo(**response["data"])

    def cooldown(self, symbol: str) -> ShipCooldown | ApiError | dict:
        endpoint = self.base_endpoint + f"/{symbol}/cooldown"
        response = self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        if "data" in response.keys():
            return ShipCooldown(**response["data"])
        return response

    def dock(self, symbol: str) -> ShipNav | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/dock"
        response = self.client.send("post", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return ShipNav(**response["data"]["nav"])

    def extract(
        self, symbol: str, survey: Survey | None = None
    ) -> CooldownExtractionCargo | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/extract"
        data = None
        if survey:
            # this is ugly..is there  a better way?
            data = {"survey": json.loads(survey.model_dump_json())}
        response = self.client.send("post", endpoint, data=data)
        if "error" in response.keys():
            return ApiError(**response)
        return CooldownExtractionCargo(**response["data"])

    def get(self, symbol: str) -> Ship | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}"
        response = self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return Ship(**response["data"])

    def list(self, limit: int = 20, page: int = 1) -> List[Ship] | ApiError:
        params = {"limit": limit, "page": page}
        endpoint = self.base_endpoint
        response = self.client.send("get", endpoint, params=params)
        if "error" in response.keys():
            return ApiError(**response)
        return [Ship(**s) for s in response["data"]]

    def list_all(self) -> List[Ship] | ApiError:
        response = paginator(self.client, "get", self.base_endpoint)
        if isinstance(response, ApiError):
            return response
        return [Ship(**s) for s in response]

    def navigate(
        self, symbol: str, waypoint_symbol: str
    ) -> ShipNav | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/navigate"
        data = {"waypointSymbol": waypoint_symbol}
        response = self.client.send("post", endpoint, data=data)
        if "error" in response.keys():
            return ApiError(**response)
        return ShipNav(**response["data"]["nav"])

    def orbit(self, symbol: str) -> ShipNav | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/orbit"
        response = self.client.send("post", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return ShipNav(**response["data"]["nav"])

    def purchase(
        self, ship_type: str, waypoint_symbol: str
    ) -> AgentShipTransaction | ApiError:
        endpoint = self.base_endpoint
        data = {
            "shipType": ship_type,
            "waypointSymbol": waypoint_symbol,
        }
        response = self.client.send("post", endpoint, data=data)
        if "error" in response.keys():
            return ApiError(**response)
        return AgentShipTransaction(**response["data"])

    def refuel(self, symbol: str) -> AgentFuelTransaction | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/refuel"
        response = self.client.send("post", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return AgentFuelTransaction(**response["data"])

    def sell(
        self, symbol: str, item_symbol: str, units: int
    ) -> AgentCargoTransaction | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/sell"
        data = {"symbol": item_symbol, "units": units}
        response = self.client.send("post", endpoint, data=data)
        if "error" in response.keys():
            return ApiError(**response)
        return AgentCargoTransaction(**response["data"])

    def survey(self, symbol: str) -> CooldownSurveys | ApiError:
        endpoint = self.base_endpoint + f"/{symbol}/survey"
        response = self.client.send("post", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return CooldownSurveys(**response["data"])

    # following still need implementation
    def refine(self):
        raise NotImplemented

    def chart(self):
        raise NotImplemented

    def jettison_cargo(self):
        raise NotImplemented

    def jump(self):
        raise NotImplemented

    def patch_nav(self):
        raise NotImplemented

    def warp(self):
        raise NotImplemented

    def scan_system(self):
        raise NotImplemented

    def scan_waypoint(self):
        raise NotImplemented

    def scan_ship(self):
        raise NotImplemented

    def purchase_cargo(self):
        raise NotImplemented

    def transfer_cargo(self):
        raise NotImplemented

    def negotiate_contract(self):
        raise NotImplemented

    def get_mounts(self):
        raise NotImplemented

    def install_mounts(self):
        raise NotImplemented

    def remove_mounts(self):
        raise NotImplemented
