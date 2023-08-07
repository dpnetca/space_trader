from space_traders.space_traders import Client


class System:
    def __init__(self, client:Client, symbol: str=None) ->None:
        self.client = client
        self.base_endpoint="/systems"
        self.symbol=symbol
        self.details=None
        if self.symbol:
            self.get()


    def list (self):
        endpoint = self.base_endpoint
        res = self.client.send("get", endpoint)
        return res

    def get(self):
        endpoint = self.base_endpoint + f"/{self.symbol}"
        res = self.client.send("get", endpoint)
        self.details = res["data"]
        return res