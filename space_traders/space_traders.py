from space_traders.client import Client
from space_traders.contract import Contract
from space_traders.agent import Agent
from space_traders.ship import Ship


class SpaceTrader:
    def __init__(self, token):
        self.client=Client(token)

    def agent(self, symbol=None):
        return Agent(self.client, symbol)

    def contract(self, symbol=None):
        return Contract(self.client, symbol)
    
    def ship(self, symbol=None):
        return Ship(self.client, symbol)

    def get_status(self):
        return self.client.send("get","",auth=False)

    def register(self, name, faction, email=""):
        endpoint = "/register"
        account = {"symbol": name, "faction": faction}
        if email:
            account["email"] = email
        r = self.client.send("post", endpoint, auth=False)
        
        return r.json()
