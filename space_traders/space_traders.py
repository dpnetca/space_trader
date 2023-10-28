from typing import Callable
from .client import Client
from .api import AgentApi, ContractApi, FactionApi, ShipApi, SystemApi
from .models import Status, RegisterNewAgent
import logging

logger = logging.getLogger("SpaceTrader")


class SpaceTrader:
    def __init__(self, token: str, log_func: Callable | None = None):
        logger.info("Initializing SpaceTrader")

        self.client = Client(token, log_func)

        self.agent = AgentApi(self.client)
        self.contract = ContractApi(self.client)
        self.faction = FactionApi(self.client)
        self.ship = ShipApi(self.client)
        self.system = SystemApi(self.client)

    async def __aenter__(self) -> None:
        return self

    async def __aexit__(self, exc_type, exc_value, traceback) -> None:
        logger.info("Exiting SpaceTrader")
        await self.client.close()

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
        r = await self.client.send("post", endpoint, data=account, auth=False)

        return RegisterNewAgent(**r["data"])
