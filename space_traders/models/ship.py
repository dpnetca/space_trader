from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ShipRegistration(BaseModel):
    name: str = Field(...)
    faction_symbol: str = Field(..., alias="factionSymbol")
    role: str = Field(...)


class ShipNavRouteWaypoint(BaseModel):
    symbol: str = Field(...)
    type: str = Field(...)
    system_symbol: str = Field(..., alias="systemSymbol")
    x: int = Field(...)
    y: int = Field(...)


class ShipRequirements(BaseModel):
    power: Optional[int] = Field(None)
    crew: Optional[int] = Field(None)
    slots: Optional[int] = Field(None)


class ShipNavRoute(BaseModel):
    destination: ShipNavRouteWaypoint = Field(...)
    origin: ShipNavRouteWaypoint = Field(...)
    departure_time: datetime = Field(..., alias="departureTime")
    arrival: datetime = Field(...)


class ShipNav(BaseModel):
    system_symbol: str = Field(..., alias="systemSymbol")
    waypoint_symbol: str = Field(..., alias="waypointSymbol")
    route: ShipNavRoute = Field(...)
    status: str = Field(...)
    flight_mode: str = Field(..., alias="flightMode")


class ShipCrew(BaseModel):
    current: int = Field(...)
    required: int = Field(...)
    capacity: int = Field(...)
    rotation: str = Field(...)
    morale: int = Field(...)
    wages: int = Field(...)


class ShipFrame(BaseModel):
    symbol: str = Field(...)
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    condition: Optional[int] = Field(None)
    module_slots: Optional[int] = Field(None, alias="moduleSlots")
    mounting_points: Optional[int] = Field(None, alias="mountingPoints")
    fuel_capacity: Optional[int] = Field(None, alias="fuelCapacity")
    requirements: Optional[ShipRequirements] = Field(None)


class ShipReactor(BaseModel):
    symbol: str = Field(...)
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    condition: Optional[int] = Field(None)
    power_output: Optional[int] = Field(None, alias="powerOutput")
    requirements: Optional[ShipRequirements] = Field(None)


class ShipEngine(BaseModel):
    symbol: str = Field(...)
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    condition: Optional[int] = Field(None)
    speed: Optional[int] = Field(None)
    requirements: Optional[ShipRequirements] = Field(None)


class ShipModules(BaseModel):
    symbol: str = Field(...)
    capacity: Optional[int] = Field(None)
    range: Optional[int] = Field(None)
    name: Optional[str] = Field(None)
    description: str = Field(...)
    requirements: ShipRequirements = Field(...)


class ShipMounts(BaseModel):
    symbol: str = Field(...)
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    strength: Optional[int] = Field(None)
    deposits: Optional[list[str]] = Field(default_factory=list)
    requirements: Optional[ShipRequirements] = Field(None)


class ShipCargoInventory(BaseModel):
    symbol: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)
    units: int = Field(...)


class ShipCargo(BaseModel):
    capacity: int = Field(...)
    units: int = Field(...)
    inventory: list[ShipCargoInventory] = Field(...)


class ShipCooldown(BaseModel):
    symbol: str = Field(..., alias="shipSymbol")
    total_seconds: int = Field(..., alias="totalSeconds")
    remaining_seconds: int = Field(..., alias="remainingSeconds")
    expiration: Optional[datetime] = Field(None)


class ShipFuelConsumed(BaseModel):
    amount: int = Field(...)
    timestamp: str = Field(...)


class ShipFuel(BaseModel):
    current: int = Field(...)
    capacity: int = Field(...)
    consumed: Optional[ShipFuelConsumed] = Field(None)


class Ship(BaseModel):
    symbol: str = Field(...)
    registration: ShipRegistration = Field(...)
    nav: ShipNav = Field(...)
    crew: Optional[ShipCrew] = Field(None)
    frame: Optional[ShipFrame] = Field(None)
    reactor: Optional[ShipReactor] = Field(None)
    engine: ShipEngine = Field(...)
    cooldown: Optional[ShipCooldown] = Field(None)
    modules: Optional[list[ShipModules]] = Field(None)
    mounts: Optional[list[ShipMounts]] = Field(None)
    cargo: Optional[ShipCargo] = Field(None)
    fuel: Optional[ShipFuel] = Field(None)


class ShipExtractionYield(BaseModel):
    symbol: str = Field(...)
    units: int = Field(...)


class ShipExtraction(BaseModel):
    symbol: str = Field(..., alias="shipSymbol")
    extraction_yield: ShipExtractionYield = Field(..., alias="yield")


class ShipyardTransaction(BaseModel):
    waypoint_symbol: str = Field(..., alias="waypointSymbol")
    ship_symbol: str = Field(..., alias="shipSymbol")
    price: int = Field(...)
    agent_symbol: str = Field(..., alias="agentSymbol")
    timestamp: datetime = Field(...)


class ShipyardShip(BaseModel):
    type: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)
    purchase_price: int = Field(..., alias="purchasePrice")
    frame: ShipFrame = Field(...)
    reactor: ShipReactor = Field(...)
    engine: ShipEngine = Field(...)
    modules: list[ShipModules] = Field(...)
    mounts: list[ShipMounts] = Field(...)
    crew: ShipCrew = Field(...)


class ShipyardShipType(BaseModel):
    type: str = Field(...)


class Shipyard(BaseModel):
    symbol: str = Field(...)
    ship_types: list[ShipyardShipType] = Field(..., alias="shipTypes")
    transactions: Optional[list[ShipyardTransaction]] = Field(None)
    ships: Optional[list[ShipyardShip]] = Field(None)
