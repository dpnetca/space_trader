from pydantic import BaseModel, Field
from . import Agent, Contract, ShipCargo


class AgentContract(BaseModel):
    agent: Agent = Field(...)
    contact: Contract = Field(...)


class ContractCargo(BaseModel):
    contact: Contract = Field(...)
    cargo: ShipCargo = Field(...)
