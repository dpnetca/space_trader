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
