from space_traders.client import Client


class ContractApi:
    def __init__(self, client: Client, symbol: str = None) -> None:
        self.client = client
        self.base_endpoint = "/my/contracts"
        self.symbol = symbol
        if self.symbol:
            self.get()

    def list(self):
        endpoint = self.base_endpoint
        res = self.client.send("get", endpoint)
        return res

    def get(self):
        endpoint = self.base_endpoint + f"/{self.symbol}"
        res = self.client.send("get", endpoint)
        self.details = res["data"]
        return res

    def accept(self):
        endpoint = self.base_endpoint + f"/{self.symbol}/accept"
        res = self.client.send("post", endpoint)
        return res

    def deliver(self, ship_id, item_id, units):
        endpoint = self.base_endpoint + f"/{self.symbol}/deliver"
        data = {"shipSymbol": ship_id, "tradeSymbol": item_id, "units": units}
        res = self.client.send("post", endpoint, data=data)
        return res
