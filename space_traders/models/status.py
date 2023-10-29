from datetime import date, datetime

from pydantic import Field
from space_traders.models.base_model import Base


class Announcements(Base):
    title: str = Field(...)
    body: str = Field(...)


class MostCredits(Base):
    agent_symbol: str = Field(..., alias="agentSymbol")
    credits: int = Field(...)


class MostSubmittedCharts(Base):
    agent_symbol: str = Field(..., alias="agentSymbol")
    chart_count: int = Field(..., alias="chartCount")


class Leaderboards(Base):
    most_credits: list[MostCredits] = Field(..., alias="mostCredits")
    most_submitted_charts: list[MostSubmittedCharts] = Field(
        ..., alias="mostSubmittedCharts"
    )


class Link(Base):
    name: str = Field(...)
    url: str = Field(...)


# next allows str for testing against mock server, type should be datetime
# but mock server returns "string"
class ServerResets(Base):
    next: str | datetime = Field(...)
    frequency: str = Field(...)


class Stats(Base):
    agents: int = Field(...)
    ships: int = Field(...)
    systems: int = Field(...)
    waypoints: int = Field(...)


# reset_date allows str for testing against mock server, type should be date
# but mock server returns "string"
class Status(Base):
    status: str = Field(...)
    version: str = Field(...)
    reset_date: str | date = Field(..., alias="resetDate")
    description: str = Field(...)
    stats: Stats = Field(...)
    leaderboards: Leaderboards = Field(...)
    server_resets: ServerResets = Field(..., alias="serverResets")
    announcements: list[Announcements] = Field(...)
    links: list[Link] = Field(...)
