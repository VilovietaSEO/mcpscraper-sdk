from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AccessListKeysInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier used to resolve the active vault and per-session state. Optional; defaults to the current MCP session.")
    vault: str | None = Field(None, alias="vault", description="Filter to keys entitled to this vault. Optional; omit to list across all vaults.")
    plan: str | None = Field(None, alias="plan", description="Filter to keys on this plan (free/pro/team/enterprise). Optional; omit to list all plans.")


class AccessListKeysOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the listing succeeded; false on auth/scope error.")
    keys: list[dict[str, Any]] | None = Field(None, alias="keys", description="Key metadata for the caller identity. NEVER includes secrets. Present when ok is true.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
