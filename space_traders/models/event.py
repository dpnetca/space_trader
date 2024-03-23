# from datetime import datetime
# from typing import Optional

from pydantic import Field
from space_traders.models.base_model import Base


class Event(Base):
    symbol: str = Field(...)
    component: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)
