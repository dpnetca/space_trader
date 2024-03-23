from pydantic import Field
from typing import Optional
from space_traders.models.base_model import Base

from .agent import Agent
from .contract import Contract
from .event import Event
from .faction import Faction
from .meta import Meta
from .market import MarketTransaction
from .fleet import (
    RepairTransaction,
    ScrapTransaction,
    Ship,
    ShipCargo,
    ShipCooldown,
    ShipExtraction,
    ShipFuel,
    ShipMount,
    ShipNav,
    ShipSiphon,
    ShipyardTransaction,
    ShipModificationTransaction,
    RefinedGood,
)
from .system import System
from .survey import Survey
from .waypoint import Chart, ConstructionSite, Waypoint


class AgentContract(Base):
    agent: Agent = Field(...)
    contract: Contract = Field(...)


class AgentCargoTransaction(Base):
    agent: Agent = Field(...)
    cargo: ShipCargo = Field(...)
    transaction: MarketTransaction = Field(...)


class AgentFuelTransaction(Base):
    agent: Agent = Field(...)
    fuel: ShipFuel = Field(...)
    transaction: MarketTransaction = Field(...)


class AgentMountCargoTransaction(Base):
    agent: Agent = Field(...)
    mounts: list[ShipMount] = Field(...)
    cargo: ShipCargo = Field(...)
    transaction: ShipModificationTransaction = Field(...)


class AgentScrapTransaction(Base):
    agent: Agent = Field(...)
    transaction: ScrapTransaction = Field(...)


class AgentRepairTransaction(Base):
    agent: Agent = Field(...)
    transaction: RepairTransaction = Field(...)


class AgentShipTransaction(Base):
    agent: Agent = Field(...)
    ship: Ship = Field(...)
    transaction: ShipyardTransaction = Field(...)


class CargoCooldownProducedConsumed(Base):
    cargo: ShipCargo = Field(...)
    cooldown: ShipCooldown = Field(...)
    produced: list[RefinedGood] = Field(...)
    consumed: list[RefinedGood] = Field(...)


class ChartWaypoint(Base):
    chart: Chart = Field(...)
    waypoint: Waypoint = Field(...)


class ContractCargo(Base):
    contract: Contract = Field(...)
    cargo: ShipCargo = Field(...)


class ConstructionCargo(Base):
    construction: ConstructionSite = Field(...)
    cargo: ShipCargo = Field(...)


class CooldownExtractionCargoEvent(Base):
    cooldown: ShipCooldown = Field(...)
    extraction: ShipExtraction = Field(...)
    cargo: ShipCargo = Field(...)
    events: list[Event] = Field(...)


class CooldownSiphonCargoEvent(Base):
    cooldown: ShipCooldown = Field(...)
    siphon: ShipSiphon = Field(...)
    cargo: ShipCargo = Field(...)
    events: list[Event] = Field(...)


class NavCooldownTransactionAgent(Base):
    nav: ShipNav = Field(...)
    cooldown: ShipCooldown = Field(...)
    transaction: MarketTransaction = Field(...)
    agent: Agent = Field(...)


class CooldownShips(Base):
    cooldown: ShipCooldown = Field(...)
    ships: list[Ship] = Field(...)


class CooldownSurveys(Base):
    cooldown: ShipCooldown = Field(...)
    surveys: list[Survey] = Field(...)


class CooldownSystems(Base):
    cooldown: ShipCooldown = Field(...)
    systems: list[System] = Field(...)


class CooldownWaypoints(Base):
    cooldown: ShipCooldown = Field(...)
    waypoints: list[Waypoint] = Field(...)


class FuelNavEvent(Base):
    fuel: ShipFuel = Field(...)
    nav: ShipNav = Field(...)
    events: Optional[list[Event]] = Field(None)


class RegisterNewAgent(Base):
    agent: Agent = Field(...)
    contract: Contract = Field(...)
    faction: Faction = Field(...)
    ship: Ship = Field(...)
    token: str = Field(...)
