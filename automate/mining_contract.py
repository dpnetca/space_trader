from datetime import datetime
from time import sleep

from space_traders.space_traders import SpaceTrader
from space_traders.ship import Ship
from space_traders.contract import Contract
from space_traders.waypoints import Waypoint


class Automate:
    def __init__(
        self,
        st: SpaceTrader,
        ship: Ship = None,
        contract: Contract = None,
        mining_location: Waypoint = None,
    ):
        if ship is None:
            ship_list = st.ship().list()
            print(ship_list)
            # TODO do soemthing here to select a ship....
        else:
            self.ship = ship

        if contract is None:
            contract_list = st.contract().list()
            print(contract_list)
            # TODO do soemthing here to select a ship....
        else:
            self.contract = contract

        self.mining_location = mining_location

    def goto_mining_location(self):
        self.ship.get()

    def navigate(self, waypoint_symbol):
        r = self.ship.navigate(waypoint_symbol)
        arrival = r["data"]["nav"]["route"]["arrival"]
        arrival_time = datetime.fromisoformat(arrival)
        now = datetime.now().astimezone()
        delta = (arrival_time - now).total_seconds()
        print(f"navigating to {waypoint_symbol} arriving in {delta} seconds")
        sleep(delta)
