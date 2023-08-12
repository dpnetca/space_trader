from pydantic import BaseModel, Field

from . import (
    Agent,
    Contract,
    MarketTransaction,
    Ship,
    ShipCargo,
    ShipCooldown,
    ShipExtraction,
    ShipFuel,
    ShipyardTransaction,
)


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
