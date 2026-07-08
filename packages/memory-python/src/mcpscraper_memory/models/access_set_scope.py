from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AccessSetScopeInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier used to resolve the active vault and per-session state. Optional; defaults to the current MCP session.")
    key_id: str = Field(..., alias="keyId", description="Identifier of the key to modify (from access-list-keys). Must be a key the caller owns.")
    scope: dict[str, Any] | None = Field(None, alias="scope", description="New scope set. Partial; the provided keys are normalized and REPLACE the full existing scope. Optional, but supply scope and/or plan.")
    plan: Literal["free", "pro", "team", "enterprise"] | None = Field(None, alias="plan", description="New subscription plan. Optional, but supply scope and/or plan.")


class AccessSetScopeOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the change applied; false on auth/scope error, not-found, or nothing-to-change.")
    key_id: str | None = Field(None, alias="keyId", description="The key that was targeted.")
    updated: bool | None = Field(None, alias="updated", description="True if a row was actually updated.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
