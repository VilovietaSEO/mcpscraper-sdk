from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class MemorySearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier used to resolve the active vault and per-session state. Optional; defaults to the current MCP session.")
    vault: str | None = Field(None, alias="vault", description="Narrow the search to exactly this vault. Optional; when omitted (the default and recommended usage) every vault the caller is entitled to is searched in one call.")
    query: str = Field(..., alias="query", description="The semantic search query — YOUR reformulation of what the human wants, not their raw message verbatim. Expand ambiguous references, add relevant synonyms/entities. Must be non-empty.")
    user_message: str | None = Field(None, alias="userMessage", description="The human's original, unmodified message that prompted this search. Optional but recommended — recorded for retrieval-quality review, does not affect the search.")
    top_k: int | None = Field(None, alias="topK", description="Maximum number of chunks to return. Optional; default 8, range 1-50.")
    include_shared: bool | None = Field(None, alias="includeShared", description="Whether to also search notes individually shared with you and accepted. Default true.")


class MemorySearchOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the search ran; false on auth/scope or backend error.")
    vault: str | None = Field(None, alias="vault", description="Present only when a single vault was searched (vault was given). Absent when every entitled vault was searched — use each result's own \"vault\" field instead.")
    vaults_searched: list[str] | None = Field(None, alias="vaultsSearched", description="Every vault handle included in this search.")
    results: list[dict[str, Any]] | None = Field(None, alias="results", description="Most-relevant chunks ordered by score, across every vault searched plus accepted shares. Present when ok is true; may be empty.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
