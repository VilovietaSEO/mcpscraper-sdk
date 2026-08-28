from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GmailSearchMessagesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_id: str = Field(..., alias="connectionId", description="A tenant-owned Gmail connectionId returned by list_service_connections.")
    query: str = Field(..., alias="query", description="Standard Gmail search query for messages; use gmail_search_contacts when the desired result is a deduplicated sender list.")
    limit: int | None = Field(None, alias="limit", description="Maximum message previews in this page; use the returned opaque cursor for another bounded page.")
    cursor: str | None = Field(None, alias="cursor", description="Opaque owner-bound cursor returned by a prior identical gmail_search_messages query; never pass a provider page token.")


class GmailSearchMessagesOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    messages: list[dict[str, Any]] = Field(..., alias="messages", description="")
    estimated_matches: Any = Field(..., alias="estimatedMatches", description="")
    complete: bool = Field(..., alias="complete", description="")
    truncated: bool = Field(..., alias="truncated", description="")
    next_cursor: Any = Field(..., alias="nextCursor", description="")
    untrusted_content: bool = Field(..., alias="untrustedContent", description="")
    error: Any = Field(..., alias="error", description="")
