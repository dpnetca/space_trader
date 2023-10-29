from datetime import datetime

from pydantic import Field
from space_traders.models.base_model import Base


class SurveyDeposit(Base):
    symbol: str = Field(...)


class Survey(Base):
    signature: str = Field(...)
    symbol: str = Field(...)
    deposits: list[SurveyDeposit] = Field(...)
    expiration: datetime = Field(...)
    size: str = Field(...)
