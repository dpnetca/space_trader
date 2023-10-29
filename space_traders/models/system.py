from pydantic import Field
from space_traders.models.base_model import Base
from typing import Optional


class SystemWaypoint(Base):
    symbol: str = Field(...)
    type: str = Field(...)
    x: int = Field(...)
    y: int = Field(...)


class SystemFaction(Base):
    symbol: str = Field(...)


class System(Base):
    symbol: str = Field(...)
    sector_symbol: str = Field(..., alias="sectorSymbol")
    type: str = Field(...)
    x: int = Field(...)
    y: int = Field(...)
    waypoints: Optional[list[SystemWaypoint]] = Field(None)
    factions: Optional[list[SystemFaction]] = Field(None)
    distance: Optional[int] = Field(None)
