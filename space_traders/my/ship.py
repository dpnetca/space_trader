from space_traders.space_traders import SpaceTraders

class Ship(SpaceTraders):
    def list(self):
        url = self.base_url + "/my/contracts"
        res = self.send("get", url)
        return res
