import os
from dotenv import load_dotenv
from space_traders.contract import Contract, Client

load_dotenv()

class SpaceTrader:
    def __init__(self, token):
        self.client=Client(token)

    def contract(self, symbol=None):
        return Contract(self.client, symbol)
        

# class Contract:
#     def __init__(self, session, symbol=None):
#         self.client = session
#         if symbol:
#             self.get(symbol)
#         else:
#             self.symbol = symbol
    
#     def get(self, symbol):
#         print(f"get {symbol}")
#         self.symbol = symbol
#         self.client.send("GET", "some-url", headers={"Content-Type": "something-else"}, somearg="yarg")


game = SpaceTrader(os.getenv("ST_TOKEN"))

c= game.contract()
print(c.list())

# contract = game.contract()
# # print(contract.session.token)


# con = game.contract("yyy")
# # print(con.symbol)
# # print(con.session.token)
