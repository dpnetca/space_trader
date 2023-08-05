import requests

from space_traders.my.agent import Agent
from space_traders.space_traders import SpaceTraders


class Client(SpaceTraders):
    def __init__(self, token=None):
        super().__init__()
        self.agent = Agent(token)

    def get_status(self):
        return self.send("get", self.base_url)

    def register(self, name, faction, email=""):
        url = self.base_url + "/register"
        account = {"symbol": name, "action": faction}
        if email:
            account["email"] = email
        # self.post
        response = requests.post(
            url, json=account, timeout=self.requests_timeout
        )

        return response.json()
