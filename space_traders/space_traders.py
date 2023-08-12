from space_traders.api import AgentApi
from space_traders.client import Client
from space_traders.api import ContractApi
from space_traders.api import ShipApi
from space_traders.api.system_api import SystemApi


class SpaceTrader:
    def __init__(self, token):
        self.client = Client(token)

    def agent_api(self):
        return AgentApi(self.client)

    def contract_api(self):
        return ContractApi(self.client)

    def ship_api(self):
        return ShipApi(self.client)

    def system_api(self):
        return SystemApi(self.client)

    def get_status(self):
        return self.client.send("get", "", auth=False)

    def register(self, name, faction, email=""):
        endpoint = "/register"
        account = {"symbol": name, "faction": faction}
        if email:
            account["email"] = email
        r = self.client.send("post", endpoint, auth=False)

        return r.json()
