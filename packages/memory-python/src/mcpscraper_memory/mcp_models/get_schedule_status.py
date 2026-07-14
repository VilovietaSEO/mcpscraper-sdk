from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GetScheduleStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")


class GetScheduleStatusOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    enabled: bool | None = Field(None, alias="enabled", description="")
    billing_mode: str | None = Field(None, alias="billingMode", description="")
    run_base_credits: float | None = Field(None, alias="runBaseCredits", description="")
    llm_cost_multiplier: float | None = Field(None, alias="llmCostMultiplier", description="")
    quota_per_period: float | None = Field(None, alias="quotaPerPeriod", description="")
    used_this_period: float | None = Field(None, alias="usedThisPeriod", description="")
    period_start: str | None = Field(None, alias="periodStart", description="")
    default_timezone: Any | None = Field(None, alias="defaultTimezone", description="IANA timezone applied to new schedules that name a time without a zone; null means UTC.")
    code: str | None = Field(None, alias="code", description="Machine-readable reason scheduling is unavailable.")
    error: str | None = Field(None, alias="error", description="")
