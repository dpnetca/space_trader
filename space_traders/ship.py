from space_traders.client import Client


class Ship:
    def __init__(self, client: Client, symbol: str = None) -> None:
        self.client = client
        self.base_endpoint = "/my/ships"
        self.details = None
        self.symbol = symbol
        if symbol:
            self.get()

    def list(self):
        endpoint = self.base_endpoint
        res = self.client.send("get", endpoint)
        return res

    def purchase(self, ship_type, waypoint_symbol):
        endpoint = self.base_endpoint
        data = {
            "shipType": ship_type,
            "waypointSymbol": waypoint_symbol,
        }
        res = self.client.send("post", endpoint, data=data)
        return res

    def get(self):
        endpoint = self.base_endpoint + f"/{self.symbol}"
        res = self.client.send("get", endpoint)
        self.details = res["data"]
        return res

    def orbit(self):
        endpoint = self.base_endpoint + f"/{self.symbol}/orbit"
        res = self.client.send("post", endpoint)
        return res

    def navigate(self, waypoint_symbol):
        endpoint = self.base_endpoint + f"/{self.symbol}/navigate"
        data = {"waypointSymbol": waypoint_symbol}
        res = self.client.send("post", endpoint, data=data)
        return res

    def dock(self):
        endpoint = self.base_endpoint + f"/{self.symbol}/dock"
        res = self.client.send("post", endpoint)
        return res

    def refuel(self):
        endpoint = self.base_endpoint + f"/{self.symbol}/refuel"
        res = self.client.send("post", endpoint)
        return res

    def extract(self):
        endpoint = self.base_endpoint + f"/{self.symbol}/extract"
        res = self.client.send("post", endpoint)
        return res

    def cargo(self):
        endpoint = self.base_endpoint + f"/{self.symbol}/cargo"
        res = self.client.send("get", endpoint)
        return res

    def sell(self, item_symbol, units):
        endpoint = self.base_endpoint + f"/{self.symbol}/sell"
        data = {"symbol": item_symbol, "units": units}
        res = self.client.send("post", endpoint, data=data)
        return res
