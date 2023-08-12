import logging
import os
from logging.handlers import RotatingFileHandler
from argparse import ArgumentParser
from dotenv import load_dotenv
from datetime import datetime
from time import sleep

# from automate.mining_contract import Automate
from space_traders.space_traders import SpaceTrader
from space_traders.models import ApiError

load_dotenv()

handler = RotatingFileHandler(
    filename="dev-log.log", maxBytes=2000000, backupCount=10
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

# parser = ArgumentParser()
# parser.add_argument("-s", "--ship", dest="ship", help="ship symbol")
# parser.add_argument(
#     "-c", "--contract", dest="contract", help="contract symbol"
# )
# args = parser.parse_args()

token = os.getenv("ST_TOKEN")

if not token:
    print("token not found...")

st = SpaceTrader(token)
sysapi = st.system_api()
waypoints = sysapi.list_waypoints("X1-YA22")
# for wp in waypoints:
#     print(f"{wp.symbol}")
#     print(wp.type)
#     for trait in wp.traits:
#         print(f"{trait.name}")
#     print()

# shipyard = sysapi.get_shipyard("X1-YA22", "X1-YA22-18767C")

# print(shipyard)

jumpgate = sysapi.get_jumpgate(waypoint_symbol="X1-YA22-66849X")
print(jumpgate)
