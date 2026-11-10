from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class DescribeServiceConnectionToolInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_id: str = Field(..., alias="connectionId", description="A tenant-owned connectionId from list_service_connections.")
    tool: str = Field(..., alias="tool", description="One exact name from that connection's readTools or actionTools. Admin-blocked and arbitrary names are rejected.")
    fresh: bool | None = Field(None, alias="fresh", description="Bypass the short-lived sanitized schema cache. Ownership, connection state, and tool policy are still rechecked; use only when a provider tool catalog just changed.")


class DescribeServiceConnectionToolOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    tool: dict[str, Any] | None = Field(None, alias="tool", description="")
    retryable: bool | None = Field(None, alias="retryable", description="")
    error_code: str | None = Field(None, alias="errorCode", description="")
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
