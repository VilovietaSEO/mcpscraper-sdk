from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AnalyticsVerifyLiveEventDefinitionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    definition_id: str = Field(..., alias="definitionId", description="Browser event-definition identifier returned by analytics_list_event_definitions.")
    timeout_ms: int | None = Field(None, alias="timeoutMs", description="Bounded wait for a newly persisted matching event.")
    max_age_seconds: int | None = Field(None, alias="maxAgeSeconds", description="Maximum accepted age of the persisted matching event.")


class AnalyticsVerifyLiveEventDefinitionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    verification: dict[str, Any] | None = Field(None, alias="verification", description="")
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
