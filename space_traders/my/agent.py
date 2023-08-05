from space_traders.space_traders import SpaceTraders


class Agent(SpaceTraders):
    # def __init__(self, token=None):
    #     self.token = token

    def get_agent(self) -> dict:
        url = self.base_url + "/my/agent"
        res = self.send("get", url)
        return res
