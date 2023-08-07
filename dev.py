import os
from dotenv import load_dotenv
# from space_traders.contract import Contract, Client

from space_traders.space_traders import SpaceTrader
load_dotenv()

game = SpaceTrader(os.getenv("ST_TOKEN"))

c_symbol = "clkyhwdvj06l9s60ceuyi4upj"
c = game.contract(c_symbol)
print(c.details)

a = game.agent()
print(a.symbol)