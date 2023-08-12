import logging
import os
from logging.handlers import RotatingFileHandler
from argparse import ArgumentParser
from dotenv import load_dotenv
from datetime import datetime

# from automate.mining_contract import Automate
from space_traders.space_traders import SpaceTrader


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
contract_api = st.contract_api()
print(contract_api.list_all())
