from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class GmailPrepareSelectionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_id: str = Field(..., alias="connectionId", description="A tenant-owned Gmail connectionId returned by list_service_connections.")
    purpose: Literal['export', 'mailbox_action', 'memory_import'] = Field(..., alias="purpose", description="The one downstream workflow this immutable selection authorizes. Choose export to download the frozen messages, mailbox_action to change them, or memory_import to preserve them in Memory. Native worker exports use the same export purpose through signed internal requests.")
    source: Any = Field(..., alias="source", description="Choose exactly one query or explicit-message-ID source; invalid mixed modes are rejected.")


class GmailPrepareSelectionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    selection: dict[str, Any] | None = Field(None, alias="selection", description="")
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
