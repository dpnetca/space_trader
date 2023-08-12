from space_traders.client import Client
from space_traders.models import Ship, ShipNav
from typing import List


class ShipApi:
    def __init__(self, client: Client) -> None:
        self.client = client
        self.base_endpoint = "/my/ships"

    def get(self, symbol: str) -> Ship:
        endpoint = self.base_endpoint + f"/{symbol}"
        res = self.client.send("get", endpoint)
        ship_data = res["data"]
        return Ship(**ship_data)

    def list(self) -> List[Ship]:
        endpoint = self.base_endpoint
        res = self.client.send("get", endpoint)
        ships_data = res["data"]
        ships = [Ship(**s) for s in ships_data]
        return ships

    def purchase(self, ship_type: str, waypoint_symbol: str) -> Ship:
        endpoint = self.base_endpoint
        data = {
            "shipType": ship_type,
            "waypointSymbol": waypoint_symbol,
        }
        res = self.client.send("post", endpoint, data=data)
        ship_data = res["data"]
        return Ship(**ship_data)

    def orbit(self, symbol: str) -> ShipNav:
        endpoint = self.base_endpoint + f"/{symbol}/orbit"
        res = self.client.send("post", endpoint)
        if "data" in res.keys():
            return ShipNav(**res["data"]["nav"])
        return res

    def navigate(self, symbol: str, waypoint_symbol: str) -> ShipNav:
        endpoint = self.base_endpoint + f"/{symbol}/navigate"
        data = {"waypointSymbol": waypoint_symbol}
        res = self.client.send("post", endpoint, data=data)
        return res

    def dock(self, symbol):
        endpoint = self.base_endpoint + f"/{symbol}/dock"
        res = self.client.send("post", endpoint)
        return res

    def refuel(self, symbol):
        endpoint = self.base_endpoint + f"/{symbol}/refuel"
        res = self.client.send("post", endpoint)
        return res

    def extract(self, symbol):
        endpoint = self.base_endpoint + f"/{symbol}/extract"
        res = self.client.send("post", endpoint)
        return res

    def cargo(self, symbol):
        endpoint = self.base_endpoint + f"/{symbol}/cargo"
        res = self.client.send("get", endpoint)
        return res

    def sell(self, symbol, item_symbol, units):
        endpoint = self.base_endpoint + f"/{symbol}/sell"
        data = {"symbol": item_symbol, "units": units}
        res = self.client.send("post", endpoint, data=data)
        return res

    def cooldown(self, symbol):
        endpoint = self.base_endpoint + f"/{symbol}/cooldown"
        res = self.client.send("get", endpoint)
        return res
