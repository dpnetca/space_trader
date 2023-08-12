from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Chart(BaseModel):
    waypoint_symbol: Optional[str] = Field(None, alias="waypointSymbol")
    submitted_by: Optional[str] = Field(None, alias="submittedBy")
    submitted_on: Optional[datetime] = Field(None, alias="submittedOn")


class ConnectedSystems(BaseModel):
    symbol: str = Field(...)
    sector_symbol: str = Field(..., alias="sectorSymbol")
    type: str = Field(...)
    faction_symbol: str = Field(..., alias="factionSymbol")
    x: int = Field(...)
    y: int = Field(...)
    distance: int = Field(...)


class Jumpgate(BaseModel):
    jump_range: int = Field(..., alias="jumpRange")
    faction_symbol: str = Field(..., alias="factionSymbol")
    connected_systems: list[ConnectedSystems] = Field(
        ..., alias="connectedSystems"
    )


class WaypointOrbitals(BaseModel):
    symbol: str = Field(...)


class WaypointFaction(BaseModel):
    symbol: str = Field(...)


class WaypointTrait(BaseModel):
    symbol: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)


class Waypoint(BaseModel):
    symbol: str = Field(...)
    type: str = Field(...)
    system_symbol: str = Field(..., alias="systemSymbol")
    x: int = Field(...)
    y: int = Field(...)
    orbitals: list[WaypointOrbitals] = Field(...)
    faction: Optional[WaypointFaction] = Field(None)
    traits: list[WaypointTrait] = Field(...)
    chart: Optional[Chart] = Field(None)
