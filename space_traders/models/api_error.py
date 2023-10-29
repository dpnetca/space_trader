from typing import Optional

from pydantic import Field
from space_traders.models.base_model import Base

"""
 Catching all error data responses could be tough and result in alot of "None"
 For now store in a general dict, review later...
"""
# class ApiErrorData(Base):
#     limit: Optional[list] = Field(None)
#     page: Optional[list] = Field(None)


class ApiErrorDetail(Base):
    message: str = Field(...)
    code: int = Field(...)
    data: Optional[dict] = Field(None)


class ApiError(Base):
    error: ApiErrorDetail = Field(...)
