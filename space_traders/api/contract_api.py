from typing import List

from space_traders.client import Client
from space_traders.models import (
    AgentContract,
    ApiError,
    Contract,
    ContractCargo,
)
from space_traders.utils import paginator


class ContractApi:
    def __init__(self, client: Client) -> None:
        self.client = client
        self.base_endpoint = "/my/contracts"

    async def accept_contract(
        self, contract_id: str
    ) -> AgentContract | ApiError:
        endpoint = self.base_endpoint + f"/{contract_id}/accept"
        response = await self.client.send("post", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return AgentContract(**response["data"])

    async def deliver_cargo_to_contract(
        self,
        contract_id: str,
        ship_id: str,
        item_id: str,
        units: int,
    ) -> ContractCargo | ApiError:
        endpoint = self.base_endpoint + f"/{contract_id}/deliver"
        data = {"shipSymbol": ship_id, "tradeSymbol": item_id, "units": units}
        response = await self.client.send("post", endpoint, data=data)
        if "error" in response.keys():
            return ApiError(**response)
        return ContractCargo(**response["data"])

    async def fulfill_contract(
        self, contract_id: str
    ) -> AgentContract | ApiError:
        endpoint = self.base_endpoint + f"/{contract_id}/fulfill"
        response = await self.client.send("post", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return AgentContract(**response["data"])

    async def get_contract(self, contract_id: str) -> Contract | ApiError:
        endpoint = self.base_endpoint + f"/{contract_id}"
        response = await self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return Contract(**response["data"])

    async def list_all_contracts(self) -> List[Contract] | ApiError:
        response = await paginator(self.client, "get", self.base_endpoint)
        if isinstance(response, ApiError):
            return response
        return [Contract(**c) for c in response]
