from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class PollChannelInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    vault: str = Field(..., alias="vault", description="The channel (vault) to poll.")
    since: str | None = Field(None, alias="since", description="ISO-8601 timestamp to override the server-remembered cursor. Optional; omit to use (and then advance) your own last-poll cursor for this channel.")


class PollChannelOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True on success; false on auth/scope error.")
    since: str | None = Field(None, alias="since", description="The cursor this poll was measured from (your previous last_polled_at, or the override you passed).")
    polled_at: str | None = Field(None, alias="polledAt", description="The new cursor value, now stored — your next no-argument poll starts from here.")
    new_messages: list[dict[str, Any]] | None = Field(None, alias="newMessages", description="New top-level messages since the cursor.")
    new_replies: list[dict[str, Any]] | None = Field(None, alias="newReplies", description="New thread replies since the cursor, across all threads in the channel.")
    new_reactions: list[dict[str, Any]] | None = Field(None, alias="newReactions", description="New reactions since the cursor.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
