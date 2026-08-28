from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AccessSwitchAccountInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    owner: str | None = Field(None, alias="owner", description="Identity whose account to make active. Must be your own identity (switch back) or one that has invited you. Omit to just list available accounts.")


class AccessSwitchAccountOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth/scope error.")
    active_owner: str | None = Field(None, alias="activeOwner", description="The account now active for your identity (your own identity means your own account).")
    is_own_account: bool | None = Field(None, alias="isOwnAccount", description="True when the active account is your own.")
    available: list[str] | None = Field(None, alias="available", description="Identities whose accounts you can switch into (you have been invited).")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
