from pydantic import BaseModel, Field
from typing import Optional


class SystemWaypoint(BaseModel):
    symbol: str = Field(...)
    type: str = Field(...)
    x: int = Field(...)
    y: int = Field(...)


class SystemFaction(BaseModel):
    symbol: str = Field(...)


class System(BaseModel):
    symbol: str = Field(...)
    sector_symbol: str = Field(..., alias="sectorSymbol")
    type: str = Field(...)
    x: int = Field(...)
    y: int = Field(...)
    waypoints: Optional[list[SystemWaypoint]] = Field(None)
    factions: Optional[list[SystemFaction]] = Field(None)
