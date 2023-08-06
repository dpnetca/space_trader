import os
from time import sleep
from datetime import datetime

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


destination = contract["data"]["terms"]["deliver"][0]["destinationSymbol"]
        
# # ship = st.ship.navigate(ship_id,destination)
# # arrival_time = ship["data"]["nav"]["arrival"]
# # print(ship)
# ship = st.ship.dock(ship_id)
# ship =  st.ship.refuel(ship_id)

# # cargo = st.ship.cargo(ship_id)
# # for item in cargo["data"]["inventory"]:
# #     ship = st.contract.deliver(contract_id,ship_id, item["symbol"], item["units"])
# #     print(ship)

# ship = st.ship.orbit(ship_id)
# ship = st.ship.navigate(ship_id, asteriod_field)
# print(ship)
# arrival_time = ship["data"]["nav"]["route"]["arrival"]
# print(arrival_time)

# ship = st.ship.dock(ship_id)
# ship =  st.ship.refuel(ship_id)
# ship = st.ship.orbit(ship_id)



while True:
    ship = st.ship.extract(ship_id)
    print(ship)
    extracted_symbol = ship["data"]["extraction"]["yield"]["symbol"]
    sleep(ship["data"]["cooldown"]["remainingSeconds"])

    
    if extracted_symbol == contract["data"]["terms"]["deliver"][0]["tradeSymbol"]:
        destination = contract["data"]["terms"]["deliver"][0]["destinationSymbol"]
        ship = st.ship.navigate(ship_id,destination)
        print(ship)
        arrival = ship["data"]["nav"]["route"]["arrival"]

        arrival_time = datetime.fromisoformat(arrival)
        now =  datetime.now().astimezone()
        delta = (arrival_time-now).total_seconds()
        print(delta)
        sleep(delta)

        ship = st.ship.dock(ship_id)
        ship = st.ship.refuel(ship_id)

        cargo = st.ship.cargo(ship_id)
        for item in cargo["data"]["inventory"]:
            ship = st.contract.deliver(contract_id,ship_id, item["symbol"], item["units"])
            print(ship)
        if ship["data"]["contract"]["terms"]["deliver"][0]["unitsRequired"] <=  ship["data"]["contract"]["terms"]["deliver"][0]["unitsFulfilled"]:
            break

        ship = st.ship.orbit(ship_id)
        ship = st.ship.navigate(ship_id, asteriod_field)
        print(ship)
        arrival = ship["data"]["nav"]["route"]["arrival"]

        arrival_time = datetime.fromisoformat(arrival)
        now =  datetime.now().astimezone()
        delta = (arrival_time-now).total_seconds()
        print(delta)
        sleep(delta)
        
        ship = st.ship.dock(ship_id)
        ship = st.ship.refuel(ship_id)
        ship = st.ship.orbit(ship_id)

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

