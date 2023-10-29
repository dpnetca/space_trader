from datetime import datetime
from typing import Optional

from pydantic import Field
from space_traders.models.base_model import Base


class Chart(Base):
    waypoint_symbol: Optional[str] = Field(None, alias="waypointSymbol")
    submitted_by: Optional[str] = Field(None, alias="submittedBy")
    submitted_on: Optional[datetime] = Field(None, alias="submittedOn")


class ConstructionMaterial(Base):
    trade_symbol: str = Field(..., alias="tradeSymbol")
    required: int = Field(...)
    fulfilled: int = Field(...)


class ConstructionSite(Base):
    symbol: str = Field(...)
    materials: list[ConstructionMaterial] = Field(...)
    is_complete: bool = Field(..., alias="isComplete")


class Jumpgate(Base):
    connections: list[str] = Field(...)


class WaypointOrbitals(Base):
    symbol: str = Field(...)


class WaypointFaction(Base):
    symbol: str = Field(...)


class WaypointTrait(Base):
    symbol: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)


class Waypoint(Base):
    symbol: str = Field(...)
    type: str = Field(...)
    system_symbol: str = Field(..., alias="systemSymbol")
    x: int = Field(...)
    y: int = Field(...)
    orbitals: list[WaypointOrbitals] = Field(...)
    orbits: Optional[str] = Field(None)
    faction: Optional[WaypointFaction] = Field(None)
    traits: list[WaypointTrait] = Field(...)
    chart: Optional[Chart] = Field(None)
