from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class MemoryListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier used to resolve the active vault and per-session state. Optional; defaults to the current MCP session.")
    vault: str | None = Field(None, alias="vault", description="Vault to list. Optional; defaults to the session active vault, then the first vault the caller is entitled to.")
    kind: Literal["note", "library", "capture", "decision"] | None = Field(None, alias="kind", description="Filter to a single note kind. Optional; omit to list every kind in the vault.")
    tags: list[str] | None = Field(None, alias="tags", description="Filter to notes tagged with any of these tags (matches the note's tags primitive). Optional; omit to not filter by tag.")


class MemoryListOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the listing succeeded; false on an auth/scope/lookup error.")
    vault: str | None = Field(None, alias="vault", description="The vault that was actually listed (after defaulting).")
    notes: list[dict[str, Any]] | None = Field(None, alias="notes", description="The notes in the vault (metadata only, no content). Present when ok is true.")
    vaults: list[str] | None = Field(None, alias="vaults", description="All vaults the caller is entitled to, for choosing a different vault to list.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
