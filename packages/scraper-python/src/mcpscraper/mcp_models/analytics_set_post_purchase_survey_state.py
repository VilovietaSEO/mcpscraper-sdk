from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsSetPostPurchaseSurveyStateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Authorized Analytics Site id.")
    survey_id: str = Field(..., alias="surveyId", description="Owner-bound survey id.")
    revision: int = Field(..., alias="revision", description="Exact survey revision being changed.")
    state: Literal['published', 'paused', 'archived'] = Field(..., alias="state", description="Publish or pause this revision. Archive is irreversible.")
    approved_copy_id: Any | None = Field(None, alias="approvedCopyId", description="Approved privacy disclosure identifier required for production publication; it is not legal approval by itself.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Retry key; reuse only for this exact mutation.")


class AnalyticsSetPostPurchaseSurveyStateOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    operation: str = Field(..., alias="operation", description="")
    survey: dict[str, Any] = Field(..., alias="survey", description="")
