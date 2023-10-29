from datetime import datetime
from typing import Optional

from pydantic import Field
from space_traders.models.base_model import Base


class ContractPayment(Base):
    on_accepted: int = Field(..., alias="onAccepted")
    on_fulfilled: int = Field(..., alias="onFulfilled")


class ContractDeliver(Base):
    trade_symbol: str = Field(..., alias="tradeSymbol")
    destination_symbol: str = Field(..., alias="destinationSymbol")
    units_required: int = Field(..., alias="unitsRequired")
    units_fulfilled: int = Field(..., alias="unitsFulfilled")


class ContractTerms(Base):
    deadline: datetime = Field(...)
    payment: ContractPayment = Field(...)
    deliver: Optional[list[ContractDeliver]] = Field(None)


class Contract(Base):
    id: str = Field(...)
    faction_symbol: str = Field(..., alias="factionSymbol")
    type: str = Field(...)
    terms: ContractTerms = Field(...)
    accepted: bool = Field(...)
    fulfilled: bool = Field(...)
    deadline_to_accept: Optional[datetime] = Field(
        None, alias="deadlineToAccept"
    )
