from pydantic import BaseModel, Field
from datetime import datetime, date


class Announcements(BaseModel):
    title: str = Field(...)
    body: str = Field(...)


class MostCredits(BaseModel):
    agent_symbol: str = Field(..., alias="agentSymbol")
    credits: int = Field(...)


class MostSubmittedCharts(BaseModel):
    agent_symbol: str = Field(..., alias="agentSymbol")
    chart_count: int = Field(..., alias="chartCount")


class Leaderboards(BaseModel):
    most_credits: list[MostCredits] = Field(..., alias="mostCredits")
    most_submitted_charts: list[MostSubmittedCharts] = Field(
        ..., alias="mostSubmittedCharts"
    )


class Link(BaseModel):
    name: str = Field(...)
    url: str = Field(...)


class ServerResets(BaseModel):
    next: datetime = Field(...)
    frequency: str = Field(...)


class Stats(BaseModel):
    agents: int = Field(...)
    ships: int = Field(...)
    systems: int = Field(...)
    waypoints: int = Field(...)


class Status(BaseModel):
    status: str = Field(...)
    version: str = Field(...)
    reset_date: date = Field(..., alias="resetDate")
    description: str = Field(...)
    stats: Stats = Field(...)
    leaderboards: Leaderboards = Field(...)
    server_resets: ServerResets = Field(..., alias="serverResets")
    announcements: list[Announcements] = Field(...)
    links: list[Link] = Field(...)
