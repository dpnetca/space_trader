import asyncio
import logging
import os
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

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
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

token = os.getenv("ST_TOKEN")

if not token:
    print("token not found...")

st = SpaceTrader(token)
status = asyncio.run(st.get_status())
print(status.reset_date)
