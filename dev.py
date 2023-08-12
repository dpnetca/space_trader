import asyncio
import logging
import os
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
from time import time

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


async def qt(ref, st, x):
    status = await st.get_status()
    print(f"{x} - {status.reset_date} - {time() - ref:5.2f} ")


async def main():
    ref = time()
    token = os.getenv("ST_TOKEN")
    if not token:
        print("token not found...")
        exit(1)

    st = SpaceTrader(token)
    async with asyncio.TaskGroup() as tg:
        [tg.create_task(qt(ref, st, x)) for x in range(20)]

    await st.client.client.aclose()


if __name__ == "__main__":
    asyncio.run(main())
