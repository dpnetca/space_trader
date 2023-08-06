from space_traders.space_traders import SpaceTraders


class Contract(SpaceTraders):
    # def __init__(self, token=None):
    #     pass

    def list(self):
        url = self.base_url + "/my/contracts"
        res = self.send("get", url)
        return res

    def get(self, contract_id):
        url = self.base_url + f"/my/contracts/{contract_id}"
        res = self.send("get", url)
        return res

    def accept(self, contract_id):
        url = self.base_url + f"/my/contracts/{contract_id}/accept"
        res = self.send("post", url)
        return res

    def deliver(self, contract_id, ship_id, item_id, units):
        url = self.base_url + f"/my/contracts/{contract_id}/deliver"
        data = {
            "shipSymbol": ship_id,
            "tradeSymbol": item_id,
            "units": units
        }
        res = self.send("post", url, data)
        return res
