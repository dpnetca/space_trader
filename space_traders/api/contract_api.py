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

    def accept(self, contract_id: str) -> AgentContract:
        endpoint = self.base_endpoint + f"/{contract_id}/accept"
        response = self.client.send("post", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return AgentContract(**response["data"])

    def deliver(
        self,
        contract_id: str,
        ship_id: str,
        item_id: str,
        units: str,
    ) -> ContractCargo:
        endpoint = self.base_endpoint + f"/{contract_id}/deliver"
        data = {"shipSymbol": ship_id, "tradeSymbol": item_id, "units": units}
        response = self.client.send("post", endpoint, data=data)
        if "error" in response.keys():
            return ApiError(**response)
        return ContractCargo(**response["data"])

    def fulfill(self, contract_id: str) -> AgentContract:
        endpoint = self.base_endpoint + f"/{contract_id}/fulfill"
        response = self.client.send("post", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return AgentContract(**response["data"])

    def get(self, contract_id: str) -> Contract:
        endpoint = self.base_endpoint + f"/{contract_id}"
        response = self.client.send("get", endpoint)
        if "error" in response.keys():
            return ApiError(**response)
        return Contract(**response["data"])

    def list(self, limit: int = 20, page: int = 1) -> List[Contract]:
        params = {"limit": limit, "page": page}
        endpoint = self.base_endpoint
        response = self.client.send("get", endpoint, params=params)
        if "error" in response.keys():
            return ApiError(**response)
        return [Contract(**c) for c in response["data"]]

    def list_all(self) -> List[Contract]:
        contracts = paginator(self.client, "get", self.base_endpoint)
        if isinstance(contracts, ApiError):
            return ApiError
        return [Contract(**c) for c in contracts]
