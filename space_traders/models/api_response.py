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
    ShipyardTransaction,
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
    mounts: ShipMounts = Field(...)
    cargo: ShipCargo = Field(...)
    transaction: MarketTransaction = Field(...)


class AgentShipTransaction(BaseModel):
    agent: Agent = Field(...)
    ship: Ship = Field(...)
    transaction: ShipyardTransaction = Field(...)


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


class CooldownNav(BaseModel):
    cooldown: ShipCooldown = Field(...)
    nav: ShipNav = Field(...)


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


class ListAgents(BaseModel):
    data: list[Agent] = Field(...)
    meta: Meta = Field(...)


class ListContracts(BaseModel):
    data: list[Contract] = Field(...)
    meta: Meta = Field(...)


class ListFactions(BaseModel):
    data: list[Faction] = Field(...)
    meta: Meta = Field(...)


class ListShips(BaseModel):
    data: list[Ship] = Field(...)
    meta: Meta = Field(...)


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
