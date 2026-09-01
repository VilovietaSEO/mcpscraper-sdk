from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsGetImpactReportInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Authorized Analytics Site id.")
    survey_id: str = Field(..., alias="surveyId", description="Published or paused post-purchase survey whose immutable responses supply the reported ledger.")
    base_model: Literal['first_touch', 'last_touch', 'last_non_direct', 'linear', 'time_decay', 'position_based', 'custom_weighted'] = Field(..., alias="baseModel", description="Existing observed attribution model; observed_plus_reported is deliberately not an observed model.")
    observed_weight_micros: int = Field(..., alias="observedWeightMicros", description="Observed share in micros. It must total exactly 1,000,000 with reportedWeightMicros.")
    reported_weight_micros: int = Field(..., alias="reportedWeightMicros", description="Customer-reported share in micros. It must total exactly 1,000,000 with observedWeightMicros.")
    methodology_version: str = Field(..., alias="methodologyVersion", description="Immutable methodology selected after reading analytics_get_attribution_methodology.")
    from_: str | None = Field(None, alias="from", description="Inclusive observed-evidence start. Omit with to for the last 30 days.")
    to: str | None = Field(None, alias="to", description="Exclusive observed-evidence end. Omit to use now.")
    click_window: Any | None = Field(None, alias="clickWindow", description="Independent observed click window.")
    view_window: Any | None = Field(None, alias="viewWindow", description="Independent view window; provider-unavailable state never manufactures view touches.")


class AnalyticsGetImpactReportOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    impact: dict[str, Any] = Field(..., alias="impact", description="")
