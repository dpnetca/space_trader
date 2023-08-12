from pydantic import BaseModel, Field

from .agent import Agent
from .contract import Contract
from .faction import Faction
from .market import MarketTransaction
from .ship import (
    Ship,
    ShipCargo,
    ShipCooldown,
    ShipExtraction,
    ShipFuel,
    ShipyardTransaction,
)
from .survey import Survey


class AgentContract(BaseModel):
    agent: Agent = Field(...)
    contact: Contract = Field(...)


class AgentCargoTransaction(BaseModel):
    agent: Agent = Field(...)
    cargo: ShipCargo = Field(...)
    transaction: MarketTransaction = Field(...)


class AgentFuelTransaction(BaseModel):
    agent: Agent = Field(...)
    fuel: ShipFuel = Field(...)
    transaction: MarketTransaction = Field(...)


class AgentShipTransaction(BaseModel):
    agent: Agent = Field(...)
    ship: Ship = Field(...)
    transaction: ShipyardTransaction = Field(...)


class ContractCargo(BaseModel):
    contact: Contract = Field(...)
    cargo: ShipCargo = Field(...)


class CooldownExtractionCargo(BaseModel):
    cooldown: ShipCooldown = Field(...)
    extraction: ShipExtraction = Field(...)
    cargo: ShipCargo = Field(...)


class CooldownSurveys(BaseModel):
    cooldown: ShipCooldown = Field(...)
    surveys: list[Survey] = Field(...)


class RegisterNewAgent(BaseModel):
    agent: Agent = Field(...)
    contract: Contract = Field(...)
    faction: Faction = Field(...)
    ship: Ship = Field(...)
    tiken: str = Field(...)
