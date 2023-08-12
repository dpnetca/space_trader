from datetime import datetime

from pydantic import BaseModel, Field


class SurveyDeposit(BaseModel):
    symbol: str = Field(...)


class Survey(BaseModel):
    signature: str = Field(...)
    symbol: str = Field(...)
    deposits: list[SurveyDeposit] = Field(...)
    expiration: datetime = Field(...)
    size: str = Field(...)
