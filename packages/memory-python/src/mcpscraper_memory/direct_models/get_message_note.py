from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GetMessageNoteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    vault: str = Field(..., alias="vault", description="The channel (vault) the message is in.")
    message_id: str = Field(..., alias="messageId", description="The message (from list-channel-messages / poll-channel) whose attached note to read.")


class GetMessageNoteOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the note was found and readable; false on auth/scope/not-found error.")
    note: dict[str, Any] | None = Field(None, alias="note", description="Present when ok is true.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
