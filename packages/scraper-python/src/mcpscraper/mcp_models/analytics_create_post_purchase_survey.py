from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AnalyticsCreatePostPurchaseSurveyInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Authorized Analytics Site id.")
    name: str = Field(..., alias="name", description="Owner-facing survey name.")
    question: str = Field(..., alias="question", description="Customer-visible structured influence question; do not request contact data or free text.")
    selection_mode: Literal['single', 'multiple'] = Field(..., alias="selectionMode", description="Whether a respondent may select one influence or several.")
    eligible_outcome_families: list[str] = Field(..., alias="eligibleOutcomeFamilies", description="Authoritative outcome families eligible to receive an invitation.")
    exchange_ttl_seconds: int = Field(..., alias="exchangeTtlSeconds", description="Short-lived merchant exchange-code lifetime.")
    session_ttl_seconds: int = Field(..., alias="sessionTtlSeconds", description="Hosted survey session lifetime after one-time exchange.")
    approved_copy_id: Any | None = Field(None, alias="approvedCopyId", description="Versioned privacy disclosure approval. A draft may omit it; production publication may not.")
    options: list[dict[str, Any]] = Field(..., alias="options", description="Two to twenty stable structured influences.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Retry key; reuse only for this exact mutation.")


class AnalyticsCreatePostPurchaseSurveyOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    operation: str | None = Field(None, alias="operation", description="")
    survey: dict[str, Any] | None = Field(None, alias="survey", description="")
    created: bool | None = Field(None, alias="created", description="")
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
