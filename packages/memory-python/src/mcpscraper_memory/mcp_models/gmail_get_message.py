from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class GmailGetMessageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_id: str = Field(..., alias="connectionId", description="The same tenant-owned Gmail connectionId used to discover this message.")
    message_id: str = Field(..., alias="messageId", description="One Gmail messageId returned by gmail_search_messages or a frozen selection preview.")
    include_raw_artifact: bool | None = Field(None, alias="includeRawArtifact", description="Keep true when complete RFC 822 fidelity or later export is required; large content is returned through an owned artifact, never silently truncated.")


class GmailGetMessageOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    message: dict[str, Any] | None = Field(None, alias="message", description="")
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
