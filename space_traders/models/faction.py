from pydantic import Field
from space_traders.models.base_model import Base


class FactionTrait(Base):
    symbol: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)


class Faction(Base):
    symbol: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)
    headquarters: str = Field(...)
    traits: list[FactionTrait] = Field(...)
    is_recruiting: bool = Field(..., alias="isRecruiting")
