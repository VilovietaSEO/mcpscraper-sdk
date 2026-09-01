from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsGetPostPurchaseSurveyReportInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Authorized Analytics Site id.")
    survey_id: str = Field(..., alias="surveyId", description="Owner-bound survey id.")


class AnalyticsGetPostPurchaseSurveyReportOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    report: dict[str, Any] = Field(..., alias="report", description="")
