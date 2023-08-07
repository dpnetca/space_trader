import os
from dotenv import load_dotenv
# from space_traders.contract import Contract, Client

from space_traders.space_traders import SpaceTrader
load_dotenv()

game = SpaceTrader(os.getenv("ST_TOKEN"))

c_symbol = "clkyhwdvj06l9s60ceuyi4upj"
c = game.contract(c_symbol)
# print(c.details)

ship = game.ship("SIKAYN-3")
# print(ship.details)


# ship.symbol = "SIKAYN-3"
# r = ship.get()
# print(ship.details)

# r = ship.dock()
# print(r)
items = ship.cargo()["data"]["inventory"]
# print(items)

for item in items:
    r = ship.sell(item["symbol"], item["units"])
    print(r)