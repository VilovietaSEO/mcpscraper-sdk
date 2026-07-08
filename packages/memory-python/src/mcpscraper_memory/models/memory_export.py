from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class MemoryExportInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier used to resolve the active vault and per-session state. Optional; defaults to the current MCP session.")
    vault: str | None = Field(None, alias="vault", description="Vault to export. Optional; defaults to the session active vault, then the first vault the caller is entitled to.")


class MemoryExportOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the export succeeded; false on auth/scope error.")
    vault: str | None = Field(None, alias="vault", description="The vault that was actually exported (after defaulting).")
    count: float | None = Field(None, alias="count", description="Total number of notes returned in the dump.")
    notes: list[dict[str, Any]] | None = Field(None, alias="notes", description="Every note in the vault with full content. Present when ok is true. Can be large.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
