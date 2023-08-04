import requests


class SpaceTraders:
    def __init__(self, token=None):
        self.base_url = "https://api.spacetraders.io/v2"
        self.token = token

    def get_status(self):
        status = requests.get(self.base_url)
        status.raise_for_status()
        return status.json()

    def register(self, name, faction, email=""):
        url = self.base_url + "/register"
        account = {"symbol": name, "action": faction}
        if email:
            account["email"] = email
        response = requests.post(url, json=account)
        response.raise_for_status()
        return response.json()

    def get_my_agent(self) -> dict:
        url = self.base_url + "/my/agent"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(url, headers=headers)
        if response.ok:
            self.my_agent: dict = response.json()["data"]
            return ""
        else:
            return response.json()["error"]
