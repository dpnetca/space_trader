import os
import logging
from logging.handlers import RotatingFileHandler

from dotenv import load_dotenv

from space_traders.space_traders import SpaceTrader
from automate.mining_contract import Automate

load_dotenv()


handler = RotatingFileHandler(
    filename="log.log", maxBytes=2000000, backupCount=10
)
logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    handlers=[handler],
    level=logging.DEBUG,
    datefmt="%Y-%m-%d %H:%M:%S",
)
# logging.basicConfig(filename="log.log", level=logging.DEBUG)
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


token = os.getenv("ST_TOKEN")
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

auto.sell_threshold = 0.5
auto.deliver_threshold = 0.1

auto.run()
