from pydantic import BaseModel, Field

from .agent import Agent
from .contract import Contract
from .faction import Faction
from .meta import Meta
from .market import MarketTransaction
from .ship import (
    Ship,
    ShipCargo,
    ShipCooldown,
    ShipExtraction,
    ShipFuel,
    ShipMounts,
    ShipNav,
    ShipSiphon,
    ShipyardTransaction,
    ShipModificationTransaction,
    RefinedGood,
)
from .system import System
from .survey import Survey
from .waypoint import Chart, Waypoint


class AgentContract(BaseModel):
    agent: Agent = Field(...)
    contract: Contract = Field(...)


class AgentCargoTransaction(BaseModel):
    agent: Agent = Field(...)
    cargo: ShipCargo = Field(...)
    transaction: MarketTransaction = Field(...)


class AgentFuelTransaction(BaseModel):
    agent: Agent = Field(...)
    fuel: ShipFuel = Field(...)
    transaction: MarketTransaction = Field(...)


class AgentMountCargoTransaction(BaseModel):
    agent: Agent = Field(...)
    mounts: list[ShipMounts] = Field(...)
    cargo: ShipCargo = Field(...)
    transaction: ShipModificationTransaction = Field(...)


class AgentShipTransaction(BaseModel):
    agent: Agent = Field(...)
    ship: Ship = Field(...)
    transaction: ShipyardTransaction = Field(...)


class CargoCooldownProducedConsumed(BaseModel):
    cargo: ShipCargo = Field(...)
    cooldown: ShipCooldown = Field(...)
    produced: list[RefinedGood] = Field(...)
    consumed: list[RefinedGood] = Field(...)


class ChartWaypoint(BaseModel):
    chart: Chart = Field(...)
    waypoint: Waypoint = Field(...)


class ContractCargo(BaseModel):
    contract: Contract = Field(...)
    cargo: ShipCargo = Field(...)


class CooldownExtractionCargo(BaseModel):
    cooldown: ShipCooldown = Field(...)
    extraction: ShipExtraction = Field(...)
    cargo: ShipCargo = Field(...)


class CooldownSiphonCargo(BaseModel):
    cooldown: ShipCooldown = Field(...)
    siphon: ShipSiphon = Field(...)
    cargo: ShipCargo = Field(...)


class NavCooldownTransaction(BaseModel):
    nav: ShipNav = Field(...)
    cooldown: ShipCooldown = Field(...)
    transaction: MarketTransaction = Field(...)


class CooldownShips(BaseModel):
    cooldown: ShipCooldown = Field(...)
    ships: list[Ship] = Field(...)


class CooldownSurveys(BaseModel):
    cooldown: ShipCooldown = Field(...)
    surveys: list[Survey] = Field(...)


class CooldownSystems(BaseModel):
    cooldown: ShipCooldown = Field(...)
    systems: list[System] = Field(...)


class CooldownWaypoints(BaseModel):
    cooldown: ShipCooldown = Field(...)
    waypoints: list[Waypoint] = Field(...)


class FuelNav(BaseModel):
    fuel: ShipFuel = Field(...)
    nav: ShipNav = Field(...)


class ListSystems(BaseModel):
    data: list[System] = Field(...)
    meta: Meta = Field(...)


class ListWaypoints(BaseModel):
    data: list[Waypoint] = Field(...)
    meta: Meta = Field(...)


class RegisterNewAgent(BaseModel):
    agent: Agent = Field(...)
    contract: Contract = Field(...)
    faction: Faction = Field(...)
    ship: Ship = Field(...)
    token: str = Field(...)
