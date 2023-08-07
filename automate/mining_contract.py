from datetime import datetime
from time import sleep
import math

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
        asteroid_field: Waypoint = None,
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
            # TODO do soemthing here to select a contract....
        else:
            self.contract = contract

        self.asteroid_field = asteroid_field
        self.sell_threshold = 0.9
        self.deliver_threshold = 0.8

    def _goto_asteroid_field(self):
        current_location = self.ship.details["nav"]["waypointSymbol"]
        current_status = self.ship.details["nav"]["status"]
        if current_location != self.asteroid_field.symbol:
            if current_status != "IN_ORBIT":
                self._orbit()
            self._navigate(self.asteroid_field.symbol)
            self._dock()
            self._refuel()
            self._orbit()


    def _navigate(self, waypoint_symbol):
        r = self.ship.navigate(waypoint_symbol)
        arrival = r["data"]["nav"]["route"]["arrival"]
        arrival_time = datetime.fromisoformat(arrival)
        now = datetime.now().astimezone()
        delta = (arrival_time - now).total_seconds()
        delta = math.ceil(delta)
        print(f"Navigating {self.ship.symbol} to {waypoint_symbol} arriving in {delta} seconds")
        sleep(delta)
    
    def _orbit(self):
        print(f"Moving {self.ship.symbol} to orbit")
        self.ship.orbit()
    
    def _dock(self):
        print(f"Docking {self.ship.symbol}")
        self.ship.dock()

    def _refuel(self):
        print(f"Refueling {self.ship.symbol}")
        self.ship.refuel()

    def _prep(self):
        self.contract_symbols = [x["tradeSymbol"] for x in self.contract.details["terms"]["deliver"]]
        self.ship.get()
        if self.ship.details["fuel"]["current"] < self.ship.details["fuel"]["capacity"]:
            self._dock()
            self._refuel()
            self._orbit()
        self._goto_asteroid_field()


    def _extract(self):
        while True:
            r = self.ship.extract()
            if "error" in r.keys():
                print(r["error"]["message"])
                remaining_seconds = r["error"]["data"]["cooldown"]["remainingSeconds"]
                print(f"waiting {remaining_seconds} seconds")
                sleep(remaining_seconds)
                continue

            extracted_symbol = r["data"]["extraction"]["yield"]["symbol"]
            extracted_units = r["data"]["extraction"]["yield"]["units"]
            print(f"extracted: {extracted_units} - {extracted_symbol}")
            remaining_seconds = r["data"]["cooldown"]["remainingSeconds"]
            cargo_units = r["data"]["cargo"]["units"]
            cargo_capacity = r["data"]["cargo"]["capacity"]
            cargo_utilized = cargo_units / cargo_capacity
            if cargo_utilized >= self.sell_threshold:
                break

            print(f"Cargo Utilized = {cargo_utilized*100:0.1f}% ({cargo_units}/{cargo_capacity})")
            print(f"waiting {remaining_seconds} seconds")
            sleep(remaining_seconds)
            print()
            
# r = ship.dock()
# cargo = ship.cargo()
# for item in cargo["data"]["inventory"]:
    # if item["symbol"] not in contract_symbols:
    #     r = ship.sell(item["symbol"], item["units"])
    #     transaction = r["data"]["transaction"]
    #     print(
    #         f"Sold {transaction['units']} {transaction['tradeSymbol']} for {transaction['pricePerUnit']} ea. ({transaction['totalPrice']} total)"
    #     )
# remaining_cargo = r["data"]["cargo"]
# cargo_capacity_remaining = (
# remaining_cargo["capacity"] - remaining_cargo["units"]
# )
# r = ship.orbit()
    def _sell(self):
        self._dock()
        cargo = self.ship.cargo()
        for item in cargo["data"]["inventory"]:
            if item["symbol"] not in self.contract_symbols:
                r = self.ship.sell(item["symbol"], item["units"])
                transaction = r["data"]["transaction"]
                print(f"Sold {transaction['units']} {transaction['tradeSymbol']} for {transaction['pricePerUnit']} ea. ({transaction['totalPrice']} total)")
        self._orbit()

    def run(self):
        self._prep()
        while True:
            self._extract()
            self._sell()
            break

        print("Automation Loop Complete")


