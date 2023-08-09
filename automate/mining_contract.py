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
        departure = r["data"]["nav"]["route"]["departureTime"]
        departure_time = datetime.fromisoformat(departure)
        # now = datetime.now().astimezone()
        delta = (arrival_time - departure_time).total_seconds()
        delta = math.ceil(delta)
        print(
            f"Navigating {self.ship.symbol} to {waypoint_symbol} "
            f"arriving in ~{delta} seconds ({arrival_time})"
        )
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
        self.contract_symbols = [
            x["tradeSymbol"] for x in self.contract.details["terms"]["deliver"]
        ]
        self.ship.get()
        if (
            self.ship.details["fuel"]["current"]
            < self.ship.details["fuel"]["capacity"]
        ):
            self._dock()
            self._refuel()
            self._orbit()
        self._goto_asteroid_field()

    def _extract(self):
        while True:
            r = self.ship.extract()
            if "error" in r.keys():
                print(r["error"]["message"])
                remaining_seconds = r["error"]["data"]["cooldown"][
                    "remainingSeconds"
                ]
                self._cooldown_delay(remaining_seconds)
                # print(f"waiting {remaining_seconds} seconds")
                # sleep(remaining_seconds)
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

            print(
                "Cargo Utilized = "
                f"{cargo_utilized*100:0.1f}% ({cargo_units}/{cargo_capacity})"
            )
            self._cooldown_delay(remaining_seconds)
            # print(f"waiting {remaining_seconds} seconds")
            # sleep(remaining_seconds)
            print()

    def _sell(self):
        self._dock()
        cargo = self.ship.cargo()
        for item in cargo["data"]["inventory"]:
            if item["symbol"] not in self.contract_symbols:
                r = self.ship.sell(item["symbol"], item["units"])
                transaction = r["data"]["transaction"]
                print(
                    f"Sold {transaction['units']} "
                    f"{transaction['tradeSymbol']} for "
                    f"{transaction['pricePerUnit']} ea. "
                    f"({transaction['totalPrice']} total)"
                )
        self._orbit()

    def _deliver(self):
        self._navigate(
            self.contract.details["terms"]["deliver"][0]["destinationSymbol"]
        )
        self._dock()
        self._refuel()
        cargo = self.ship.cargo()
        for item in cargo["data"]["inventory"]:
            if item["symbol"] in self.contract_symbols:
                r = self.contract.deliver(
                    self.ship.symbol, item["symbol"], item["units"]
                )
                print(r)
                deliverables = r["data"]["contract"]["terms"]["deliver"][0]
                required = deliverables["unitsRequired"]
                fulfilled = deliverables["unitsFulfilled"]
                print(f"{fulfilled} / {required} fulfilled")
        self._orbit()
        self._navigate(self.asteroid_field.symbol)
        self._dock()
        self._refuel()
        self._orbit()

    def _cooldown_delay(self, remaining_seconds=None):
        if remaining_seconds is None:
            cooldown = self.ship.cooldown()
            if cooldown:
                remaining_seconds = cooldown["data"]["remainingSeconds"]
            else:
                remaining_seconds = 0
        if remaining_seconds > 0:
            print(f"Waiting {remaining_seconds} seconds")
            sleep(remaining_seconds)

    def run(self):
        self._prep()
        while True:
            self._cooldown_delay()
            self._extract()
            self._sell()
            cargo = self.ship.cargo()
            cargo_units = cargo["data"]["units"]
            cargo_capacity = cargo["data"]["capacity"]
            cargo_utilized = cargo_units / cargo_capacity
            if cargo_utilized >= self.deliver_threshold:
                self._deliver()
            self.contract.get()
            deliverables = self.contract.details["terms"]["deliver"][0]
            if deliverables["unitsFulfilled"] >= deliverables["unitsRequired"]:
                break
        print("Automation Loop Complete")
