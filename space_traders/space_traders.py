from space_traders.api import AgentApi
from space_traders.client import Client
from space_traders.api import ContractApi
from space_traders.api import ShipApi
from space_traders.api.system_api import SystemApi
from space_traders.api.waypoint_api import WaypointApi


class SpaceTrader:
    def __init__(self, token):
        self.client = Client(token)

    def agent_api(self):
        return AgentApi(self.client)

    def contract(self, symbol=None):
        return ContractApi(self.client, symbol)

    def ship_api(self):
        return ShipApi(self.client)

    # def system(self, symbol=None):
    #     return System(self.client, symbol)

    # def waypoint(self, system=None, symbol=None):
    #     return Waypoint(self.client, system, symbol)

    def get_status(self):
        return self.client.send("get", "", auth=False)

    def register(self, name, faction, email=""):
        endpoint = "/register"
        account = {"symbol": name, "faction": faction}
        if email:
            account["email"] = email
        r = self.client.send("post", endpoint, auth=False)

        return r.json()
