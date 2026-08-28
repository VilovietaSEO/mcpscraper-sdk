from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class DeleteNoteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier used to resolve the active vault and per-session state. Optional; defaults to the current MCP session.")
    vault: str | None = Field(None, alias="vault", description="Vault to delete from. Optional; defaults to the session active vault, then the first vault the caller is entitled to.")
    path: str | None = Field(None, alias="path", description="Exact vault-relative note path to delete, e.g. projects/q3-plan (as returned by memory-list or recall). Required unless shareId is given.")
    share_id: str | None = Field(None, alias="shareId", description="Destroy a note shared with you and you accepted, by its shareId, instead of vault+path. Requires the share to grant delete permission and baseRevision (mandatory for shared notes).")
    base_revision: float | None = Field(None, alias="baseRevision", description="Revision the delete is based on (from a prior get). When provided, the delete only applies if the note is still at this revision; otherwise it is rejected as a conflict instead of destroying a concurrent edit. Mandatory when shareId is given; optional otherwise (omit to delete unconditionally).")


class DeleteNoteOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the delete request was processed; false on an auth/scope/lookup error or a revision conflict.")
    vault: str | None = Field(None, alias="vault", description="The vault the delete was applied to (after defaulting). Present when ok is true.")
    deleted: bool | None = Field(None, alias="deleted", description="True if a note was removed; false if no matching note existed (idempotent). Present when ok is true.")
    conflict: bool | None = Field(None, alias="conflict", description="True when baseRevision did not match the current revision: someone else changed the note first. Nothing was deleted.")
    current: dict[str, Any] | None = Field(None, alias="current", description="Present only when conflict is true: the note as it stands now, so the caller can re-read before deciding whether to still delete.")
    code: str | None = Field(None, alias="code", description="Machine-readable denial code when ok is false: revision_conflict.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
