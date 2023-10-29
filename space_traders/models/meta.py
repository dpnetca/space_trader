from pydantic import Field
from space_traders.models.base_model import Base


class Meta(Base):
    total: int = Field(...)
    page: int = Field(...)
    limit: int = Field(...)
