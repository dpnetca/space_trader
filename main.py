import os
from time import sleep

from space_traders.client import Client

from dotenv import load_dotenv

load_dotenv()

token = os.getenv("ST_TOKEN")

if not token:
    print("token not found...")

st = Client(token=token)
ship_id = "SIKAYN-3"
contract_id="clkyhwdvj06l9s60ceuyi4upj"
asteriod_field = "X1-YA22-87615D"

contract = st.contract.get(contract_id)
print(contract)

while True:

    ship = st.ship.extract(ship_id)
    print(ship)
    sleep(ship["data"]["cooldown"]["remainingSeconds"])
    
    if ship["data"]["extraction"]["yield"]["symbol"] == contract["data"]["terms"]["deliver"][0]["tradeSymbol"]:
        destination = contract["data"]["terms"]["deliver"][0]["destinationSymbol"]
        st.ship.navigate(ship_id,destination)
        ship = st.ship.dock(ship_id)
        st.contract.deliver(contract_id, ship_id,ship["data"]["extraction"]["yield"]["symbol"], ship["data"]["extraction"]["yield"]["units"])
        ship = st.ship.orbit(ship_id)
        ship = st.ship.navigate(ship_id, asteriod_field)
        ship = st.ship.dock(ship_id)
        ship =  st.ship.refuel(ship_id)
        ship = st.ship.orbit(ship_id)

        break
    else:
        ship = st.ship.dock(ship_id)
        # print(ship)
        cargo = st.ship.cargo(ship_id)
        for item in cargo["data"]["inventory"]:
            ship = st.ship.sell(ship_id, item["symbol"], item["units"])
            print(ship)

        ship = st.ship.orbit(ship_id)
        # print(ship)

print ("done")

