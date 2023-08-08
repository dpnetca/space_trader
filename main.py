import os
from time import sleep
from datetime import datetime

from dotenv import load_dotenv

from space_traders.space_traders import SpaceTrader

load_dotenv()

token = os.getenv("ST_TOKEN")
sell_threshold = 3
contract_deliver_threshold = 6
ship_symbol = "SIKAYN-4"
contract_symbol = "clkyhwdvj06l9s60ceuyi4upj"

if not token:
    print("token not found...")

st = SpaceTrader(token)

ship = st.ship(ship_symbol)
contract = st.contract(contract_symbol)
asteriod_field = st.waypoint(symbol="X1-YA22-87615D")

destination = st.waypoint(
    symbol=contract.details["terms"]["deliver"][0]["destinationSymbol"]
)
contract_symbols = [
    x["tradeSymbol"] for x in contract.details["terms"]["deliver"]
]
print(f"contract items: {contract_symbols}")

complete = False
while not complete:
    r = ship.extract()
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
    cargo_capacity_remaining = (
        r["data"]["cargo"]["capacity"] - r["data"]["cargo"]["units"]
    )

    # SELL THRESHOLD
    if cargo_capacity_remaining <= sell_threshold:
        r = ship.dock()
        cargo = ship.cargo()
        for item in cargo["data"]["inventory"]:
            if item["symbol"] not in contract_symbols:
                r = ship.sell(item["symbol"], item["units"])
                transaction = r["data"]["transaction"]
                print(
                    f"Sold {transaction['units']} {transaction['tradeSymbol']} for {transaction['pricePerUnit']} ea. ({transaction['totalPrice']} total)"
                )
                remaining_cargo = r["data"]["cargo"]
        cargo_capacity_remaining = (
            remaining_cargo["capacity"] - remaining_cargo["units"]
        )
        r = ship.orbit()

        cargo = ship.cargo()
        cargo_capacity_remaining = cargo["data"]["capacity"] - cargo["data"]["units"] 

        # CONTRACT DELIVERY THRESHOLD
        if cargo_capacity_remaining <= contract_deliver_threshold:
            r = ship.navigate(destination.symbol)
            print(destination.symbol)
            arrival = r["data"]["nav"]["route"]["arrival"]
            arrival_time = datetime.fromisoformat(arrival)
            now = datetime.now().astimezone()
            delta = (arrival_time - now).total_seconds()
            print(
                f"navigating to {destination.symbol} arriving in {delta} seconds"
            )
            sleep(delta)
            ship.dock()
            ship.refuel()
            for item in remaining_cargo["inventory"]:
                print(f"delivering {item['units']} {item['symbol']}")
                r = contract.deliver(
                    ship.symbol, item["symbol"], item["units"]
                )
                required = r["data"]["contract"]["terms"]["deliver"][0]["unitsRequired"]
                fulfilled = r["data"]["contract"]["terms"]["deliver"][0][
                    "unitsFulfilled"
                ]
                print(f"{fulfilled} / {required} fulfilled")
                if fulfilled >= required:
                    complete = True

            ship.orbit()
            r = ship.navigate(asteriod_field.symbol)
            arrival = r["data"]["nav"]["route"]["arrival"]
            arrival_time = datetime.fromisoformat(arrival)
            now = datetime.now().astimezone()
            delta = (arrival_time - now).total_seconds()
            print(
                f"navigating to {asteriod_field.symbol} arriving in {delta} seconds"
            )
            sleep(delta)
            ship.dock()
            ship.refuel()
            ship.orbit()
            continue

    print(f"Remaining cargo capacity = {cargo_capacity_remaining}")
    print(f"waiting {remaining_seconds} seconds")
    sleep(remaining_seconds)
    print()

print("done")
