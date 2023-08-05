import os

from space_traders.client import Client

from dotenv import load_dotenv

load_dotenv()

token = os.getenv("ST_TOKEN")

if not token:
    print("token not found...")

st = Client(token=token)

# agent = st.agent.get_agent()
# print(agent)

# err = st.my_agent.get()
# err = st.get_my_agent()

# if err:
#     print("unable to retrieve agent")
#     print(f"{err['code']} - {err['message']}")
# else:
#     print(f"Welcome {st.my_agent.symbol}")

# status = st.get_status()
# print(status)

# account = st.register("Sikayn", "COSMIC")
# print(account)

# contracts = st.contract.list()
# print(contracts)

# contract = st.contract.get("clkyhwdvj06l9s60ceuyi4upj")
# print(contract)

# contract = st.contract.accept("clkyhwdvj06l9s60ceuyi4upj")
# print(contract)

# ships = st.ship.list()
# print(ships)

# systems = st.system.list()
# for system in systems["data"]:
#     print(system)

system = st.system.get("X1-YA22")
print(system)
