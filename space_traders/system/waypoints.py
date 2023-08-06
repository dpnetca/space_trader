from space_traders.space_traders import SpaceTraders

class Waypoint(SpaceTraders):
    def list (self, system_id):
        url = self.base_url + f"/systems/{system_id}/waypoints"
        res = self.send("get", url)
        return res

    def get(self, system_id, waypoint_id):
        url = self.base_url + f"/systems/{system_id}/waypoints/{waypoint_id}"
        res = self.send("get", url)
        return res

    def shipyard(self, system_id, waypoint_id):
        url = self.base_url + f"/systems/{system_id}/waypoints/{waypoint_id}/shipyard"
        res = self.send("get", url)
        return res

    def market(self, system_id, waypoint_id):
        url = self.base_url + f"/systems/{system_id}/waypoints/{waypoint_id}/market"
        res = self.send("get", url)
        return res
