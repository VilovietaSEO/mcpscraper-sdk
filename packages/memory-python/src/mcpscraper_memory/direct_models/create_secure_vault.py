from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CreateSecureVaultInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    name: str = Field(..., alias="name", description="Vault name. Must match ^[A-Za-z0-9 _-]{1,48}$. Defaults to a name like \"Passwords\" if the caller has no preference.")


class CreateSecureVaultOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the vault was created; false on auth/scope/validation error.")
    vault: str | None = Field(None, alias="vault", description="The vault name. Present when ok is true.")
    created: bool | None = Field(None, alias="created", description="True if newly created; false if a vault with this name already existed for you (idempotent) — note this does NOT confirm the existing vault is secure-kind; check list-vaults if unsure.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
