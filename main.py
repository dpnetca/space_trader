import logging
import os
from logging.handlers import RotatingFileHandler
from argparse import ArgumentParser
from dotenv import load_dotenv

from automate.mining_contract import Automate
from space_traders.space_traders import SpaceTrader

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

parser = ArgumentParser()
parser.add_argument("-s", "--ship", dest="ship", help="ship symbol")
parser.add_argument(
    "-c", "--contract", dest="contract", help="contract symbol"
)
args = parser.parse_args()

token = os.getenv("ST_TOKEN")

if not token:
    print("token not found...")

st = SpaceTrader(token)

auto = Automate(
    st,
    st.ship(args.ship),
    st.contract(args.contract),
    st.waypoint(symbol="X1-YA22-87615D"),
)

auto.sell_threshold = 0.9
auto.deliver_threshold = 0.8

auto.run()
