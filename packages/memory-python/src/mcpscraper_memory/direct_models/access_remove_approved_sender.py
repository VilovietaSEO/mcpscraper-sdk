from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AccessRemoveApprovedSenderInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    sender_identity: str = Field(..., alias="senderIdentity", description="Identity to remove from your approved-senders list.")


class AccessRemoveApprovedSenderOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth error.")
    sender: str | None = Field(None, alias="sender", description="The identity that was removed.")
    removed: bool | None = Field(None, alias="removed", description="True when an existing approval was found and removed.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
