from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AnalyticsUpdateOnboardingPreferencesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    preferences: dict[str, Any] | None = Field(None, alias="preferences", description="Presentation-only account preferences.")
    last_presented_step: Any | None = Field(None, alias="lastPresentedStep", description="Setup step most recently presented to the account operator.")
    dismissed_help: list[str] | None = Field(None, alias="dismissedHelp", description="Help-card keys the account operator dismissed. This cannot complete evidence milestones.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.")


class AnalyticsUpdateOnboardingPreferencesOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    presentation: dict[str, Any] | None = Field(None, alias="presentation", description="")
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
