from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AccessListApprovedSendersInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")


class AccessListApprovedSendersOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth error.")
    approved_senders: list[str] | None = Field(None, alias="approvedSenders", description="Identities approved to reach you.")
    allow_unapproved_senders: bool | None = Field(None, alias="allowUnapprovedSenders", description="True if your inbox is open to anyone regardless of this list.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
