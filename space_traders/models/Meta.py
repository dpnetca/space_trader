from pydantic import BaseModel, Field


class Meta(BaseModel):
    total: int = Field(...)
    page: int = Field(...)
    limit: int = Field(...)
