from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class PostMessageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    vault: str = Field(..., alias="vault", description="The channel (vault) to post to.")
    content: str = Field(..., alias="content", description="The message text.")
    attach_note: dict[str, Any] | None = Field(None, alias="attachNote", description="Attach one of your own notes to this message, auto-shared with every current channel member. Optional.")


class PostMessageOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the message was posted; false on auth/scope error.")
    message_id: str | None = Field(None, alias="messageId", description="Path-style identifier for this message: use it as parentMessageId on reply-message, or messageId on react-message.")
    posted_at: str | None = Field(None, alias="postedAt", description="ISO-8601 timestamp the message was posted.")
    attached_note: dict[str, Any] | None = Field(None, alias="attachedNote", description="Present when attachNote was given and the share succeeded.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
