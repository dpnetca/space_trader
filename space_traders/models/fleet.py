from datetime import datetime
from typing import Optional

from pydantic import Field
from space_traders.models.base_model import Base


class RepairTransaction(Base):
    waypoint_symbol: str = Field(..., alias="waypointSymbol")
    ship_symbol: str = Field(..., alias="shipSymbol")
    total_price: int = Field(..., alias="totalPrice")
    timestamp: datetime = Field(...)


class ScrapTransaction(Base):
    waypoint_symbol: str = Field(..., alias="waypointSymbol")
    ship_symbol: str = Field(..., alias="shipSymbol")
    total_price: int = Field(..., alias="totalPrice")
    timestamp: datetime = Field(...)


class ShipRegistration(Base):
    name: str = Field(...)
    faction_symbol: str = Field(..., alias="factionSymbol")
    role: str = Field(...)


class ShipNavRouteWaypoint(Base):
    symbol: str = Field(...)
    type: str = Field(...)
    system_symbol: str = Field(..., alias="systemSymbol")
    x: int = Field(...)
    y: int = Field(...)


class ShipRequirements(Base):
    power: Optional[int] = Field(None)
    crew: Optional[int] = Field(None)
    slots: Optional[int] = Field(None)


class ShipNavRoute(Base):
    departure: Optional[ShipNavRouteWaypoint] = Field(None)  # deprecated
    destination: ShipNavRouteWaypoint = Field(...)
    origin: ShipNavRouteWaypoint = Field(...)
    departure_time: datetime = Field(..., alias="departureTime")
    arrival: datetime = Field(...)


class ShipNav(Base):
    system_symbol: str = Field(..., alias="systemSymbol")
    waypoint_symbol: str = Field(..., alias="waypointSymbol")
    route: ShipNavRoute = Field(...)
    status: str = Field(...)
    flight_mode: str = Field(..., alias="flightMode")


class ShipCrew(Base):
    current: Optional[int] = Field(None)
    required: int = Field(...)
    capacity: int = Field(...)
    rotation: Optional[str] = Field(None)
    morale: Optional[int] = Field(None)
    wages: Optional[int] = Field(None)


class ShipFrame(Base):
    symbol: str = Field(...)
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    condition: Optional[float] = Field(None)
    integrity: Optional[float] = Field(None)
    module_slots: Optional[int] = Field(None, alias="moduleSlots")
    mounting_points: Optional[int] = Field(None, alias="mountingPoints")
    fuel_capacity: Optional[int] = Field(None, alias="fuelCapacity")
    requirements: Optional[ShipRequirements] = Field(None)


class ShipReactor(Base):
    symbol: str = Field(...)
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    condition: Optional[float] = Field(None)
    integrity: Optional[float] = Field(None)
    power_output: Optional[int] = Field(None, alias="powerOutput")
    requirements: Optional[ShipRequirements] = Field(None)


class ShipEngine(Base):
    symbol: str = Field(...)
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    condition: Optional[float] = Field(None)
    integrity: Optional[float] = Field(None)
    speed: Optional[int] = Field(None)
    requirements: Optional[ShipRequirements] = Field(None)


class ShipModule(Base):
    symbol: str = Field(...)
    capacity: Optional[int] = Field(None)
    range: Optional[int] = Field(None)
    name: Optional[str] = Field(None)
    description: str = Field(...)
    production: Optional[list[str]] = Field(None)
    requirements: ShipRequirements = Field(...)


class ShipMount(Base):
    symbol: str = Field(...)
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    strength: Optional[int] = Field(None)
    deposits: Optional[list[str]] = Field(default_factory=list)
    requirements: Optional[ShipRequirements] = Field(None)


class ShipCargoInventory(Base):
    symbol: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)
    units: int = Field(...)


class ShipCargo(Base):
    capacity: int = Field(...)
    units: int = Field(...)
    inventory: list[ShipCargoInventory] = Field(...)


class ShipCooldown(Base):
    ship_symbol: str = Field(..., alias="shipSymbol")
    total_seconds: int = Field(..., alias="totalSeconds")
    remaining_seconds: int = Field(..., alias="remainingSeconds")
    expiration: Optional[datetime] = Field(None)


class ShipFuelConsumed(Base):
    amount: int = Field(...)
    timestamp: str = Field(...)


class ShipFuel(Base):
    current: int = Field(...)
    capacity: int = Field(...)
    consumed: Optional[ShipFuelConsumed] = Field(None)


class Ship(Base):
    symbol: str = Field(...)
    registration: ShipRegistration = Field(...)
    nav: ShipNav = Field(...)
    crew: Optional[ShipCrew] = Field(None)
    frame: Optional[ShipFrame] = Field(None)
    reactor: Optional[ShipReactor] = Field(None)
    engine: ShipEngine = Field(...)
    cooldown: Optional[ShipCooldown] = Field(None)
    modules: Optional[list[ShipModule]] = Field(None)
    mounts: Optional[list[ShipMount]] = Field(None)
    cargo: Optional[ShipCargo] = Field(None)
    fuel: Optional[ShipFuel] = Field(None)


class ShipExtractionYield(Base):
    symbol: str = Field(...)
    units: int = Field(...)


class ShipExtraction(Base):
    symbol: str = Field(..., alias="shipSymbol")
    extraction_yield: ShipExtractionYield = Field(..., alias="yield")


class ShipyardTransaction(Base):
    waypoint_symbol: str = Field(..., alias="waypointSymbol")
    ship_symbol: str = Field(..., alias="shipSymbol")
    shipType: str = Field(..., alias="shipType")
    price: int = Field(...)
    agent_symbol: str = Field(..., alias="agentSymbol")
    timestamp: datetime = Field(...)


class ShipyardShip(Base):
    type: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)
    supply: str = Field(...)
    activity: Optional[str] = Field(None)
    purchase_price: int = Field(..., alias="purchasePrice")
    frame: ShipFrame = Field(...)
    reactor: ShipReactor = Field(...)
    engine: ShipEngine = Field(...)
    modules: list[ShipModule] = Field(...)
    mounts: list[ShipMount] = Field(...)
    crew: ShipCrew = Field(...)


class ShipyardShipType(Base):
    type: str = Field(...)


class Shipyard(Base):
    symbol: str = Field(...)
    ship_types: list[ShipyardShipType] = Field(..., alias="shipTypes")
    transactions: Optional[list[ShipyardTransaction]] = Field(None)
    ships: Optional[list[ShipyardShip]] = Field(None)
    modifications_fee: int = Field(..., alias="modificationsFee")


class ShipModificationTransaction(Base):
    waypoint_symbol: str = Field(..., alias="waypointSymbol")
    ship_symbol: str = Field(..., alias="shipSymbol")
    trade_symbol: str = Field(..., alias="tradeSymbol")
    total_price: int = Field(..., alias="totalPrice")
    timestamp: datetime = Field(...)


class RefinedGood(Base):
    trade_symbol: str = Field(..., alias="tradeSymbol")
    units: int = Field(...)


class ShipSiphonYield(Base):
    symbol: str = Field(...)
    units: int = Field(...)


class ShipSiphon(Base):
    symbol: str = Field(..., alias="shipSymbol")
    siphon_yield: ShipSiphonYield = Field(..., alias="yield")
