from datetime import date, datetime

from pydantic import BaseModel, Field


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


# next allows str for testing against mock server, type should be datetime
# but mock server returns "string"
class ServerResets(BaseModel):
    next: str | datetime = Field(...)
    frequency: str = Field(...)


class Stats(BaseModel):
    agents: int = Field(...)
    ships: int = Field(...)
    systems: int = Field(...)
    waypoints: int = Field(...)


# reset_date allows str for testing against mock server, type should be date
# but mock server returns "string"
class Status(BaseModel):
    status: str = Field(...)
    version: str = Field(...)
    reset_date: str | date = Field(..., alias="resetDate")
    description: str = Field(...)
    stats: Stats = Field(...)
    leaderboards: Leaderboards = Field(...)
    server_resets: ServerResets = Field(..., alias="serverResets")
    announcements: list[Announcements] = Field(...)
    links: list[Link] = Field(...)
