from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


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

    ok: bool | None = Field(None, alias="ok", description="")
    operation: str | None = Field(None, alias="operation", description="")
    survey: dict[str, Any] | None = Field(None, alias="survey", description="")
    delivery: dict[str, Any] | None = Field(None, alias="delivery", description="")
    preview: str | None = Field(None, alias="preview", description="")
    scope: dict[str, Any] | None = Field(None, alias="scope", description="")
    recovery: dict[str, Any] | None = Field(None, alias="recovery", description="")

    @model_serializer(mode="wrap")
    def _serialize_response(self, handler, info):
        data = handler(self)
        for name, field in type(self).model_fields.items():
            if name not in self.model_fields_set:
                key = field.alias if info.by_alias and field.alias else name
                data.pop(key, None)
        return data
