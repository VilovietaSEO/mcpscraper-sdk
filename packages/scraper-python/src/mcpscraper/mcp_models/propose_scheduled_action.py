from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ProposeScheduledActionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    request: str = Field(..., alias="request", description="Freeform text describing what you want scheduled.")


class ProposeScheduledActionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    description: str | None = Field(None, alias="description", description="Proposed description — edit freely before confirming.")
    vault: str | None = Field(None, alias="vault", description="Proposed target vault.")
    cadence: str | None = Field(None, alias="cadence", description="Proposed cadence: once, daily, weekly, or monthly.")
    time_of_day: str | None = Field(None, alias="timeOfDay", description="Proposed 24-hour HH:MM run time, when the request named one.")
    timezone: str | None = Field(None, alias="timezone", description="Proposed IANA timezone — from the request, or the account default when the request named a time without a zone.")
    rationale: str | None = Field(None, alias="rationale", description="Why these choices were made — read this before confirming.")
    error: str | None = Field(None, alias="error", description="")
