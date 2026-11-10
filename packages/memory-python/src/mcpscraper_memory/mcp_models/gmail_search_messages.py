from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class GmailSearchMessagesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_id: str = Field(..., alias="connectionId", description="A tenant-owned Gmail connectionId returned by list_service_connections.")
    query: str = Field(..., alias="query", description="Standard Gmail search query for messages; use gmail_search_contacts when the desired result is a deduplicated sender list.")
    limit: int | None = Field(None, alias="limit", description="Maximum message previews in this page; use the returned opaque cursor for another bounded page.")
    cursor: str | None = Field(None, alias="cursor", description="Opaque owner-bound cursor returned by a prior identical gmail_search_messages query; never pass a provider page token.")


class GmailSearchMessagesOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    messages: list[dict[str, Any]] | None = Field(None, alias="messages", description="")
    estimated_matches: Any | None = Field(None, alias="estimatedMatches", description="")
    complete: bool | None = Field(None, alias="complete", description="")
    truncated: bool | None = Field(None, alias="truncated", description="")
    next_cursor: Any | None = Field(None, alias="nextCursor", description="")
    untrusted_content: bool | None = Field(None, alias="untrustedContent", description="")
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
