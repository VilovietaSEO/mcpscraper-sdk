from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ListVaultsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier used to resolve the active vault and per-session state. Optional; defaults to the current MCP session.")


class ListVaultsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the listing succeeded; false on an auth/scope error.")
    active_account: str | None = Field(None, alias="activeAccount", description="The account these vaults belong to (your own identity unless you have switched into another account).")
    is_own_account: bool | None = Field(None, alias="isOwnAccount", description="True when the active account is your own; false when you have switched into an account someone invited you to.")
    vaults: list[dict[str, Any]] | None = Field(None, alias="vaults", description="Every vault visible in the active account, with role, addressable handle, and live storage usage. Present when ok is true.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
