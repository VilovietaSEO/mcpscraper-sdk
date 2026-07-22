from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GmailSearchContactsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_id: str = Field(..., alias="connectionId", description="A Gmail connectionId from list_service_connections. Read-only — does not require actionsEnabled.")
    query: str = Field(..., alias="query", description="Gmail search syntax, e.g. \"from:brandnorth.com after:2026/03/22\" or \"brandnorth.com\".")
    max_messages: int | None = Field(None, alias="maxMessages", description="Max messages to fetch and aggregate in this call. Paginate with pageToken for more; the response reports totalMatches and truncated so undercoverage is never silent.")
    page_token: str | None = Field(None, alias="pageToken", description="Continuation token from a prior response to fetch the next page.")


class GmailSearchContactsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    total_matches: float | None = Field(None, alias="totalMatches", description="Gmail's estimated total matches for the query, independent of how many were fetched this call.")
    messages_fetched: float | None = Field(None, alias="messagesFetched", description="")
    truncated: bool | None = Field(None, alias="truncated", description="True when totalMatches exceeds messagesFetched — more results exist, use nextPageToken.")
    next_page_token: Any = Field(..., alias="nextPageToken", description="")
    messages: list[dict[str, Any]] | None = Field(None, alias="messages", description="")
    contacts: list[dict[str, Any]] | None = Field(None, alias="contacts", description="Messages deduped by sender email address, newest-to-oldest within this fetch only — not the full query result set when truncated.")
    error: Any = Field(..., alias="error", description="")
