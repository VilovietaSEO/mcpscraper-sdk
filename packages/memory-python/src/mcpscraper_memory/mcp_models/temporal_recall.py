from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class TemporalRecallInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="Vault to recall from. Optional; defaults to the session active vault, then the first vault the caller is entitled to.")
    query: str | None = Field(None, alias="query", description="Optional natural-language query; when present, a semantic search is blended into the results.")
    days_ago: int | None = Field(None, alias="daysAgo", description="Recall a single calendar day this many days ago (0 = today). Optional; ignored when from/to are given.")
    from_: str | None = Field(None, alias="from", description="Start of an explicit window (ISO-8601 / parseable date). Use together with \"to\". Overrides daysAgo.")
    to: str | None = Field(None, alias="to", description="End of an explicit window (ISO-8601 / parseable date). Use together with \"from\".")


class TemporalRecallOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when recall succeeded; false on auth/scope error.")
    range: dict[str, Any] | None = Field(None, alias="range", description="The actual time window used after resolving daysAgo/from/to (default: last 7 days).")
    items: list[dict[str, Any]] | None = Field(None, alias="items", description="Captures within the window, newest-first. Present when ok is true.")
    search_results: list[dict[str, Any]] | None = Field(None, alias="searchResults", description="Blended semantic-search hits for the query. Present only when a query was supplied.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
