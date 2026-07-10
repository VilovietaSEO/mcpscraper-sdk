from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GetScheduleStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")


class GetScheduleStatusOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    enabled: bool | None = Field(None, alias="enabled", description="")
    quota_per_period: float | None = Field(None, alias="quotaPerPeriod", description="")
    used_this_period: float | None = Field(None, alias="usedThisPeriod", description="")
    period_start: str | None = Field(None, alias="periodStart", description="")
    error: str | None = Field(None, alias="error", description="")
