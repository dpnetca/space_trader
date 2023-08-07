import os
from time import sleep
from datetime import datetime

from dotenv import load_dotenv

from space_traders.space_traders import SpaceTrader
from automate.mining_contract import Automate

load_dotenv()

token = os.getenv("ST_TOKEN")
sell_threshold = 0
contract_deliver_threshold = 10
ship_symbol = "SIKAYN-3"
contract_symbol = "clkyhwdvj06l9s60ceuyi4upj"

if not token:
    print("token not found...")

st = SpaceTrader(token)

auto = Automate(
    st,
    st.ship(ship_symbol),
    st.contract(contract_symbol),
    st.waypoint(symbol="X1-YA22-87615D"),
)

auto.run()