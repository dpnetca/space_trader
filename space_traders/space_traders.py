from .client import Client
from .api import AgentApi, ContractApi, FactionApi, ShipApi, SystemApi
from .models import Status, RegisterNewAgent


class SpaceTrader:
    def __init__(self, token):
        self.client = Client(token)

        self.agent = AgentApi(self.client)
        self.contract = ContractApi(self.client)
        self.faction = FactionApi(self.client)
        self.ship = ShipApi(self.client)
        self.system = SystemApi(self.client)

    # def agent_api(self):
    #     return AgentApi(self.client)

    # def contract_api(self):
    #     return ContractApi(self.client)

    # def ship_api(self):
    #     return ShipApi(self.client)

    # def system_api(self):
    #     return SystemApi(self.client)

    async def get_status(self) -> Status:
        status = await self.client.send("get", "", auth=False)
        return Status(**status)

    async def register(
        self, name: str, faction: str, email: str = ""
    ) -> RegisterNewAgent:
        endpoint = "/register"
        account = {"symbol": name, "faction": faction}
        if email:
            account["email"] = email
        r = await self.client.send("post", endpoint, auth=False)

        return RegisterNewAgent(**r["data"])
