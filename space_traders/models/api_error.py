from pydantic import BaseModel, Field


class ApiErrorDetail(BaseModel):
    message: str = Field(...)
    code: int = Field(...)


class ApiError(BaseModel):
    error: ApiErrorDetail = Field(...)
