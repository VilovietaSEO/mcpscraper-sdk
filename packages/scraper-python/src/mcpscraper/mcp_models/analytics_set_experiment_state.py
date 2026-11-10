from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AnalyticsSetExperimentStateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Authorized Analytics Site id.")
    experiment_id: str = Field(..., alias="experimentId", description="Owner-bound experiment id returned by analytics_create_experiment.")
    revision: int = Field(..., alias="revision", description="Exact experiment revision being changed.")
    operation: Literal['approve', 'activate_canary', 'activate', 'pause', 'kill', 'archive'] = Field(..., alias="operation", description="Approval and activation are distinct operations. Pause and kill publish rollback immediately.")
    confirmed: bool | None = Field(None, alias="confirmed", description="Required for approve, activate_canary, and activate. This confirms only the exact state transition.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Retry key; reuse only for this exact mutation.")


class AnalyticsSetExperimentStateOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    experiment: dict[str, Any] | None = Field(None, alias="experiment", description="")
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
