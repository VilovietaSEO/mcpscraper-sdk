from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AccessShareNoteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    vault: str | None = Field(None, alias="vault", description="Vault containing the note to share. Required (with path) unless shareId is given. Must be a vault you own.")
    path: str | None = Field(None, alias="path", description="Vault-relative path of the note to share. Required (with vault) unless shareId is given.")
    share_id: str | None = Field(None, alias="shareId", description="Instead of vault+path, re-share a note already shared to you by this shareId. Requires reshare permission on that share.")
    grantee_identity: str = Field(..., alias="granteeIdentity", description="Identity to offer the note to.")
    permissions: dict[str, Any] | None = Field(None, alias="permissions", description="Permissions to grant beyond read (always granted): edit (write back to the canonical note), delete (destroy the canonical note — dangerous), reshare (grantee may re-share onward). All default false.")
    bundle_links: Any | None = Field(None, alias="bundleLinks", description="true to also share every detected linked note (same permissions as this share); an array of specific link refs (path or title, from a prior call's linkCandidates) to share only those. Omit or false to share none — default, and the safest choice when unsure.")


class AccessShareNoteOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the offer was created; false on auth/scope/lookup error.")
    share_id: str | None = Field(None, alias="shareId", description="Identifier the grantee will use to accept-share, then address the note on get/put/delete.")
    grantee: str | None = Field(None, alias="grantee", description="The identity the note was offered to.")
    permissions: dict[str, Any] | None = Field(None, alias="permissions", description="The permissions in effect for this share.")
    note: str | None = Field(None, alias="note", description="Guidance: the offer is pending until the grantee calls accept-share.")
    link_candidates: list[dict[str, Any]] | None = Field(None, alias="linkCandidates", description="Notes this one links to (same vault) that were NOT bundled into this share. Relay these to the human and ask before calling share-note again with bundleLinks if they want them included — otherwise they render as [[private note]] to this grantee.")
    bundled: list[dict[str, Any]] | None = Field(None, alias="bundled", description="Linked notes that WERE bundled into this share as their own pending offers (per bundleLinks).")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
