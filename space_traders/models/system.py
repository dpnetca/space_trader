from typing import Optional

from pydantic import Field

from space_traders.models.base_model import Base


class SystemWaypointOrbitals(Base):
    symbol: str = Field(...)


class SystemWaypoint(Base):
    symbol: str = Field(...)
    type: str = Field(...)
    x: int = Field(...)
    y: int = Field(...)
    orbitals: list[SystemWaypointOrbitals] = Field(...)
    orbits: Optional[str] = Field(None)


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
