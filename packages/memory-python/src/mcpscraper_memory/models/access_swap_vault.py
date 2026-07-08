from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AccessSwapVaultInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier whose active vault is being changed. Optional; defaults to the current MCP session.")
    vault: str = Field(..., alias="vault", description="Vault to make active for the session. Must be an entitled vault and the key must hold \"swap\" scope.")


class AccessSwapVaultOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the active vault was set; false on auth/scope error.")
    active_vault: str | None = Field(None, alias="activeVault", description="The vault now active for the session.")
    session: str | None = Field(None, alias="session", description="The session the active vault was set for.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
