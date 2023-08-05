import requests

from space_traders.space_traders import SpaceTraders

from space_traders.my.agent import Agent
from space_traders.my.contract import Contract
from space_traders.my.ship import Ship
from space_traders.system.system import System

class Client(SpaceTraders):
    def __init__(self, token=None):
        super().__init__()
        self.agent = Agent(token)
        self.contract = Contract(token)
        self.ship = Ship(token)
        self.system = System(token)

    def get_status(self):
        return self.send("get", self.base_url)

    def register(self, name, faction, email=""):
        url = self.base_url + "/register"
        account = {"symbol": name, "faction": faction}
        if email:
            account["email"] = email
        # self.post
        response = requests.post(
            url, json=account, timeout=self.requests_timeout
        )

        return response.json()
