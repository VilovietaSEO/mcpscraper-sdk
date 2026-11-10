from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class ReadServiceConnectionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_id: str = Field(..., alias="connectionId", description="A connectionId from list_service_connections.")
    tool: str = Field(..., alias="tool", description="One of that connection's readTools (from list_service_connections). An unlisted tool name is rejected with the allowed list.")
    args: dict[str, Any] | None = Field(None, alias="args", description="Arguments for the tool, if it needs any (e.g. a channel id, a date filter).")


class ReadServiceConnectionOutput(BaseModel):
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
