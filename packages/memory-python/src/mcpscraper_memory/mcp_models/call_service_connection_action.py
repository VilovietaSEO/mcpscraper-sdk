from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class CallServiceConnectionActionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    confirmed: bool | None = Field(None, alias="confirmed", description="Set true only when the person explicitly authorized this exact external action. If omitted, a 2026-capable client may ask for confirmation through MCP multi-round input.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Required stable key for this intended external action. Reuse it only to retry the same action after a lost response; use a new key for a new action.")
    connection_id: str = Field(..., alias="connectionId", description="A connectionId from list_service_connections with actionsEnabled true.")
    tool: str = Field(..., alias="tool", description="One exact tool name from that connection's actionTools. Arbitrary provider action names and adminBlockedTools are rejected server-side.")
    args: dict[str, Any] = Field(..., alias="args", description="Arguments required by the selected action. The provider action validates its own typed input before execution.")


class CallServiceConnectionActionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    result: Any | None = Field(None, alias="result", description="")
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
