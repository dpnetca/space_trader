from typing import Optional

from pydantic import BaseModel, Field


class Agent(BaseModel):
    account_id: Optional[str] = Field(None, alias="accountId")
    symbol: str = Field(...)
    headquarters: str = Field(...)
    credits: int = Field(...)
    starting_faction: str = Field(..., alias="startingFaction")
    ship_count: Optional[int] = Field(None, alias="shipCount")
