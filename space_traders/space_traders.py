import logging
from typing import Callable

from .client import Client
from .models import RegisterNewAgent, Status, ApiError
from .api import AgentApi, ContractApi, FactionApi, FleetApi, SystemApi

logger = logging.getLogger("SpaceTrader")


class SpaceTrader:
    def __init__(self, token: str, log_func: Callable | None = None):
        logger.info("Initializing SpaceTrader")

        self.client = Client(token, log_func)

        self.agent = AgentApi(self.client)
        self.contract = ContractApi(self.client)
        self.faction = FactionApi(self.client)
        self.fleet = FleetApi(self.client)
        self.system = SystemApi(self.client)

    async def __aenter__(self) -> None:
        return self

    async def __aexit__(self, exc_type, exc_value, traceback) -> None:
        await self.close()

    async def close(self) -> None:
        logger.info("Exiting SpaceTrader")
        await self.client.close()

    async def get_status(self) -> Status:
        status = await self.client.send("get", "", auth=False)
        return Status(**status)

    async def register(
        self, name: str, faction: str, email: str = ""
    ) -> RegisterNewAgent | ApiError:
        endpoint = "/register"
        account = {"symbol": name, "faction": faction}
        if email:
            account["email"] = email
        r = await self.client.send("post", endpoint, data=account, auth=False)
        if "error" in r.keys():
            return ApiError(**r)
        return RegisterNewAgent(**r["data"])
