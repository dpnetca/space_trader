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
ship_api = st.ship_api()

# ship = ship_api.get("SIKAYN-1")
# survey = ship_api.survey(ship.symbol)
# survey0 = survey.surveys[0]
# print(survey0)
miner = ship_api.get("SIKAYN-4")
ship_api.dock(miner.symbol)
cargo = ship_api.cargo(miner.symbol)
for item in cargo.inventory:
    ship_api.sell(miner.symbol, item.symbol, item.units)
ship_api.orbit(miner.symbol)
# extraction = ship_api.extract(miner.symbol, survey0)
extraction = ship_api.extract(miner.symbol)
print(extraction)
