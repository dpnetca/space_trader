from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class MarketTransaction(BaseModel):
    waypoint_symbol: str = Field(..., alias="waypointSymbol")
    ship_symbol: str = Field(..., alias="shipSymbol")
    trade_symbol: str = Field(..., alias="tradeSymbol")
    type: Optional[str] = Field(None)
    units: Optional[int] = Field(None)
    price_per_unit: Optional[int] = Field(None, alias="pricePerUnit")
    total_price: int = Field(..., alias="totalPrice")
    timestamp: datetime = Field(...)


class MarketItem(BaseModel):
    symbol: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)


class MarketTradeGoods(BaseModel):
    symbol: str = Field(...)
    trade_volume: int = Field(..., alias="tradeVolume")
    supply: str = Field(...)
    purchase_price: int = Field(..., alias="purchasePrice")
    sell_price: int = Field(..., alias="sellPrice")


class Market(BaseModel):
    symbol: str
    exports: list[MarketItem] = Field(...)
    imports: list[MarketItem] = Field(...)
    exchange: list[MarketItem] = Field(...)
    transactions: Optional[list[MarketTransaction]] = Field(None)
    trade_goods: Optional[list[MarketTradeGoods]] = Field(
        None, alias="tradeGoods"
    )
