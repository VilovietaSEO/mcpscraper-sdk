from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AccessApproveSenderInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    sender_identity: str = Field(..., alias="senderIdentity", description="Identity (email or user id) to approve as a sender.")


class AccessApproveSenderOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth error.")
    sender: str | None = Field(None, alias="sender", description="The identity that was approved.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
