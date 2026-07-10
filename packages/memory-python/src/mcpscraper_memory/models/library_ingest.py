from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class LibraryIngestInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier used to resolve the active vault and per-session state. Optional; defaults to the current MCP session.")
    vault: str | None = Field(None, alias="vault", description="Vault to deposit into. Optional and normally omitted: raw scrapes always default to Library. Override only for a deliberate nonstandard migration.")
    title: str = Field(..., alias="title", description="Short human-readable title for the item; used to build the stored path. Must be non-empty.")
    content: str = Field(..., alias="content", description="The full captured text (scrape/transcript/output) to store and index. Must be non-empty.")
    source: str = Field(..., alias="source", description="Provenance of the content, e.g. a URL or tool name. Must be non-empty.")
    captured_at: str | None = Field(None, alias="capturedAt", description="ISO-8601 capture timestamp. Optional; defaults to now. Also seeds the deterministic storage path.")
    summary: str | None = Field(None, alias="summary", description="Retrieval-ready source summary. Optional; a provenance summary is generated when omitted.")
    tags: list[str] | None = Field(None, alias="tags", description="Reviewed canonical tags. Existing tags should be resolved first; when omitted, deterministic source/topic tags are generated.")
    related: list[str] | None = Field(None, alias="related", description="Reviewed same-vault Library note paths.")
    related_vault_notes: list[str] | None = Field(None, alias="relatedVaultNotes", description="Reviewed cross-vault references in Vault::path.md form.")
    local_vault_path: str | None = Field(None, alias="localVaultPath", description="Filesystem root to also mirror the item to. Optional; falls back to MEMORY_LOCAL_VAULT_ROOT env when set.")


class LibraryIngestOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the item was stored; false on auth/scope error.")
    vault: str | None = Field(None, alias="vault", description="The vault the item was stored in (after defaulting).")
    note_id: str | None = Field(None, alias="noteId", description="Internal id of the created note.")
    path: str | None = Field(None, alias="path", description="Vault-relative path the item was stored at (under library/...).")
    indexed: float | None = Field(None, alias="indexed", description="Number of search chunks indexed (0 if embedding failed but the note still saved).")
    dual_written: bool | None = Field(None, alias="dualWritten", description="True if the item was also mirrored to the local filesystem vault.")
    next_step: str | None = Field(None, alias="nextStep", description="Recommended extraction action after the raw Library source is safe.")
    code: str | None = Field(None, alias="code", description="Machine-readable denial code when ok is false: quota_exceeded or free_cost_cap.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
