from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AccessInboxSettingsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    allow_unapproved_senders: bool = Field(..., alias="allowUnapprovedSenders", description="Set true to accept invites/shares from anyone; false to require approval.")


class AccessInboxSettingsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth error.")
    allow_unapproved_senders: bool | None = Field(None, alias="allowUnapprovedSenders", description="The setting now in effect.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
