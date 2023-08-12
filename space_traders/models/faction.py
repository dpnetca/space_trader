from pydantic import BaseModel, Field


class FactionTrait(BaseModel):
    symbol: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)


class Faction(BaseModel):
    symbol: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)
    headquarters: str = Field(...)
    traits: list[FactionTrait] = Field(...)
    is_recruiting: bool = Field(..., alias="isRecruiting")
