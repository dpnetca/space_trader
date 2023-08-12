from space_traders.space_traders import Client


class WaypointApi:
    def __init__(
        self, client: Client, system: str = None, symbol: str = None
    ) -> None:
        self.client = client
        self.system = system
        self.base_endpoint = f"/systems/{self.system}"
        self.symbol = symbol
        self.details = None

        if self.symbol:
            segments = self.symbol.split("-")
            self.system = "-".join(segments[:2])
            self.base_endpoint = f"/systems/{self.system}"
            self.get()

    def list(self):
        if self.system:
            endpoint = self.base_endpoint + "/waypoints"
            res = self.client.send("get", endpoint)
            return res
        else:
            print("Error system symbol must be defined")
            return None

    def get(self):
        endpoint = self.base_endpoint + f"/waypoints/{self.symbol}"
        res = self.client.send("get", endpoint)
        self.details = res["data"]
        return res

    def shipyard(self):
        endpoint = self.base_endpoint + f"/waypoints/{self.symbol}/shipyard"
        res = self.client.send("get", endpoint)
        return res

    def market(self):
        endpoint = self.base_endpoint + f"/waypoints/{self.symbol}/market"
        res = self.client.send("get", endpoint)
        return res
