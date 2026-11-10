from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class TestServiceConnectionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_id: str = Field(..., alias="connectionId", description="A tenant-owned connectionId from list_service_connections.")
    provider_config_key: str | None = Field(None, alias="providerConfigKey", description="Optional provider hint from list_service_connections.")


class TestServiceConnectionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    operational_status: Literal['available', 'unavailable'] | None = Field(None, alias="operationalStatus", description="")
    checked_at: str | None = Field(None, alias="checkedAt", description="")
    tool_count: int | None = Field(None, alias="toolCount", description="")
    code: str | None = Field(None, alias="code", description="")
    error: Any | None = Field(None, alias="error", description="")
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
