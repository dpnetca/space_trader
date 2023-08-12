from typing import Optional

from pydantic import BaseModel, Field

"""
 Catching all error data responses could be tough and result in alot of "None"
 For now store in a general dict, review later...
"""
# class ApiErrorData(BaseModel):
#     limit: Optional[list] = Field(None)
#     page: Optional[list] = Field(None)


class ApiErrorDetail(BaseModel):
    message: str = Field(...)
    code: int = Field(...)
    data: Optional[dict] = Field(None)


class ApiError(BaseModel):
    error: ApiErrorDetail = Field(...)
