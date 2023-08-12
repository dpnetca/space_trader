from pydantic import BaseModel, Field


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
    waypoints: list[SystemWaypoint] = Field(...)
    factions: list[SystemFaction] = Field(...)
