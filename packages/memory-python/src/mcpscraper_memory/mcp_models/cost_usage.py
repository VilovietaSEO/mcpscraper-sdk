from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CostUsageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    period: str | None = Field(None, alias="period", description="Billing month as YYYY-MM. Optional; defaults to the current month.")


class CostUsageOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when usage was computed; false on auth/scope error.")
    identity: str | None = Field(None, alias="identity", description="The caller identity the costs are scoped to.")
    period: str | None = Field(None, alias="period", description="Billing month the figures cover (YYYY-MM).")
    plan: str | None = Field(None, alias="plan", description="Caller plan.")
    cost_usd: float | None = Field(None, alias="costUsd", description="Total metered cost this period in USD.")
    by_source: dict[str, Any] | None = Field(None, alias="bySource", description="Cost breakdown by source (llm/embed/storage/compute).")
    free_cap_usd: float | None = Field(None, alias="freeCapUsd", description="The free-tier monthly processing cap in USD.")
    free_cap_reached: bool | None = Field(None, alias="freeCapReached", description="True when a free caller is at/over the cap (embeds/optimization paused).")
    pro_budget_usd: float | None = Field(None, alias="proBudgetUsd", description="The Pro soft fair-use budget (price / 3) in USD.")
    total_bytes: float | None = Field(None, alias="totalBytes", description="Total stored bytes for the caller.")
    total_gb: float | None = Field(None, alias="totalGb", description="Total stored GB for the caller.")
    quota_gb: Any | None = Field(None, alias="quotaGb", description="Storage quota in GB for the caller plan. Null when the plan is unlimited.")
    unlimited: bool | None = Field(None, alias="unlimited", description="True when the caller is on the unlimited plan (no storage ceiling, exempt from the free cost cap).")
    by_tier: list[dict[str, Any]] | None = Field(None, alias="byTier", description="Operator-only: blended cost-per-user per plan for the current period.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
