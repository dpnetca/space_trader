import os

from game.space_traders import SpaceTraders

from dotenv import load_dotenv

load_dotenv()

token = os.getenv("ST_TOKEN")

if not token:
    print("token not found...")

st = SpaceTraders(token=token)

err = st.get_my_agent()

if err:
    print("unable to retrieve agent")
    print(f"{err['code']} - {err['message']}")
else:
    print(f"Welcome {st.my_agent['symbol']}")

# status = st.get_status()
# print(status)

# account = st.register("Sikayn", "COSMIC")
# print(account)
