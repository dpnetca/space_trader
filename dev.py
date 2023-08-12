import asyncio
import logging
import os
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
from time import time

from space_traders import SpaceTrader

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


async def main():
    token = os.getenv("ST_TOKEN")
    if not token:
        print("token not found...")
        exit(1)

    st = SpaceTrader(token)
    x = await st.ship.scan_ships("SIKAYN-1")
    print(x)

    await st.client.client.aclose()


if __name__ == "__main__":
    asyncio.run(main())
