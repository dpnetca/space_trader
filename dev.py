import os
from dotenv import load_dotenv
# from space_traders.contract import Contract, Client

from space_traders.space_traders import SpaceTrader
load_dotenv()

game = SpaceTrader(os.getenv("ST_TOKEN"))

c= game.contract()
print(c.list())

# contract = game.contract()
# # print(contract.session.token)


# con = game.contract("yyy")
# # print(con.symbol)
# # print(con.session.token)
