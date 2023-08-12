from pydantic import BaseModel, Field
from datetime import datetime


class MarketTransaction(BaseModel):
    waypoint_symbol: str = Field(..., alias="waypointSymbol")
    ship_symbol: str = Field(..., alias="shipSymbol")
    trade_symbol: str = Field(..., alias="tradeSymbol")
    type: str = Field(...)
    units: int = Field(...)
    price_per_unit: int = Field(..., alias="pricePerUnit")
    total_rice: int = Field(..., alias="totalPrice")
    timestamp: datetime = Field(...)
