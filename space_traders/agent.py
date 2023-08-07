from space_traders.client import Client


class Agent:
    def __init__(self, client: Client, symbol: str = None) -> None:
        self.client = client
        self.base_endpoint = "/my/agent"
        self.symbol = symbol
        if not self.symbol:
            self.get_my_agent()

    def get_my_agent(self) -> dict:
        r = self.client.send("get", self.base_endpoint)
        r = r["data"]
        self.account_id = r["accountId"]
        self.symbol = r["symbol"]
        self.headquarters = r["headquarters"]
        self.credits = r["credits"]
        self.starting_faction = r["startingFaction"]
        return r
