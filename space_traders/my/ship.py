from space_traders.space_traders import SpaceTraders


class Ship(SpaceTraders):
    def list(self):
        url = self.base_url + "/my/ships"
        res = self.send("get", url)
        return res

    def purchase(self, ship_type, waypoint_id):
        url = self.base_url + "/my/ships"
        data = {
            "shipType": ship_type,
            "waypointSymbol": waypoint_id,
        }
        res = self.send("post", url, data)
        return res

    def get(self, ship_id):
        url = self.base_url + f"/my/ships/{ship_id}"
        res = self.send("get", url)
        return res

    def orbit(self, ship_id):
        url = self.base_url + f"/my/ships/{ship_id}/orbit"
        res = self.send("post", url)
        return res

    def navigate(self, ship_id, waypoint_id):
        url = self.base_url + f"/my/ships/{ship_id}/navigate"
        data = {"waypointSymbol": waypoint_id}
        res = self.send("post", url, data)
        return res

    def dock(self, ship_id):
        url = self.base_url + f"/my/ships/{ship_id}/dock"
        res = self.send("post", url)
        return res

    def refuel(self, ship_id):
        url = self.base_url + f"/my/ships/{ship_id}/refuel"
        res = self.send("post", url)
        return res
    
    def extract(self, ship_id):
        url = self.base_url + f"/my/ships/{ship_id}/extract"
        res = self.send("post", url)
        return res

    def cargo(self, ship_id):
        url = self.base_url + f"/my/ships/{ship_id}/cargo"
        res = self.send("get", url)
        return res

    def sell(self, ship_id, item_id, units):
        url = self.base_url + f"/my/ships/{ship_id}/sell"
        data = {"symbol": item_id, "units": units}
        res = self.send("post", url, data)
        return res
