from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsUpdateOnboardingPreferencesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    preferences: dict[str, Any] | None = Field(None, alias="preferences", description="Presentation-only account preferences.")
    last_presented_step: Any | None = Field(None, alias="lastPresentedStep", description="Setup step most recently presented to the account operator.")
    dismissed_help: list[str] | None = Field(None, alias="dismissedHelp", description="Help-card keys the account operator dismissed. This cannot complete evidence milestones.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.")


class AnalyticsUpdateOnboardingPreferencesOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    presentation: dict[str, Any] = Field(..., alias="presentation", description="")
