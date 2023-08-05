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

# system = st.system.get("X1-YA22")
# print(system)1

# waypoints = st.waypoint.list("X1-YA22")
# # print(waypoints)

# for waypoint in waypoints["data"]:
#     print(f"{waypoint['symbol']} - {waypoint['type']}")
#     for trait in waypoint['traits']:
#         print(f"  - {trait['symbol']}")
#     print()

# waypoint =  st.waypoint.get("X1-YA22", "X1-YA22-18767C")
# print(waypoint)

# shipyard = st.waypoint.shipyard("X1-YA22", "X1-YA22-18767C")
# # print(shipyard)

# for ship in shipyard["data"]["shipTypes"]:
#     print(ship)
#     print()


# for ship in shipyard["data"]["ships"]:
#     print(ship)
#     print()


# ships = st.ship.list()
# print(ships)

# new_ship = st.ship.purchase("SHIP_MINING_DRONE","X1-YA22-18767C")
# print(new_ship)

ships = st.ship.list()
for ship in ships["data"]:
    print(ship)
    print()
