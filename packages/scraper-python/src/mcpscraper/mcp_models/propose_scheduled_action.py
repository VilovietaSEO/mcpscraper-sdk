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
    rationale: str | None = Field(None, alias="rationale", description="Why these choices were made — read this before confirming.")
    error: str | None = Field(None, alias="error", description="")
