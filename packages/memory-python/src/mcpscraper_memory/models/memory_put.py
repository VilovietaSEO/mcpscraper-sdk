from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class MemoryPutInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier used to resolve the active vault and per-session state. Optional; defaults to the current MCP session.")
    vault: str | None = Field(None, alias="vault", description="Vault to write to. Optional; defaults to the session active vault, then the first vault the caller is entitled to. On a default-provisioned account, pick the vault whose job matches the content (see the server instructions for the full 13-vault guide) rather than defaulting blindly — e.g. a lesson learned goes in Knowledge, the raw source it came from goes in Library, a broken feature goes in Issues, a named real-world initiative goes in Projects.")
    path: str | None = Field(None, alias="path", description="Vault-relative note path to create or overwrite, e.g. projects/q3-plan. Writing an existing path replaces it. Required unless shareId is given.")
    share_id: str | None = Field(None, alias="shareId", description="Edit a note someone individually shared with you and you accepted (accept-share), by its shareId, instead of vault+path. Requires the share to grant edit permission, and baseRevision is mandatory (get the current revision first) since you are editing alongside the owner and possibly others.")
    title: str | None = Field(None, alias="title", description="Optional human-readable title; defaults are derived from the path when omitted.")
    content: str = Field(..., alias="content", description="The full note body to store and index for semantic search. Must be non-empty.")
    props: dict[str, Any] | None = Field(None, alias="props", description="Obsidian note primitives (status, summary, tags, pinned, source_type, source_ref, related, related_vault_notes, embed, embed_priority, type, domain, folder). Stored on the note so it round-trips the vault shape; type/domain/folder also steer routing when no vault is given.")
    base_revision: float | None = Field(None, alias="baseRevision", description="Revision the edit is based on (from a prior get/put). When provided, the write only applies if the note is still at this revision; otherwise it is rejected as a conflict instead of silently overwriting a concurrent edit. Omit for last-write-wins (fine for solo notes).")


class MemoryPutOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the note was stored; false on auth/scope error, empty content, or a revision conflict.")
    note: dict[str, Any] | None = Field(None, alias="note", description="The stored note metadata. Present when ok is true.")
    indexed: float | None = Field(None, alias="indexed", description="Number of search chunks indexed for the content (0 if embedding failed but the note still saved).")
    conflict: bool | None = Field(None, alias="conflict", description="True when baseRevision did not match the current revision: someone else changed the note first. No write happened.")
    current: dict[str, Any] | None = Field(None, alias="current", description="Present only when conflict is true: the note as it stands now, so the caller can reconcile and retry without another round trip.")
    code: str | None = Field(None, alias="code", description="Machine-readable denial code when ok is false: quota_exceeded, free_cost_cap, or revision_conflict.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
