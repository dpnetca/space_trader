from space_traders.space_traders import SpaceTraders

class System(SpaceTraders):
    def list (self):
        url = self.base_url + "/systems"
        res = self.send("get", url)
        return res

    def get(self, system_id):
        url = self.base_url + f"/systems/{system_id}"
        res = self.send("get", url)
        return res
