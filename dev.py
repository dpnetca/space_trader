import os
from dotenv import load_dotenv

from space_traders.space_traders import SpaceTrader
load_dotenv()

game = SpaceTrader(os.getenv("ST_TOKEN"))

# s = game.system("X1-YA22")
# print(s.details)

wp = game.waypoint(symbol="X1-YA22-87615D")
print(wp.details)

mp = wp.market()
print(mp)