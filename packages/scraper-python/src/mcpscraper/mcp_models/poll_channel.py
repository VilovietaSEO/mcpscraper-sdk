from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class PollChannelInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str = Field(..., alias="vault", description="The channel (vault) to poll.")
    since: str | None = Field(None, alias="since", description="ISO-8601 timestamp to override the server-remembered cursor. Optional; omit to use (and then advance) your own last-poll cursor for this channel.")


class PollChannelOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="True on success; false on auth/scope error.")
    since: str | None = Field(None, alias="since", description="The cursor this poll was measured from (your previous last_polled_at, or the override you passed).")
    polled_at: str | None = Field(None, alias="polledAt", description="The new cursor value, now stored — your next no-argument poll starts from here.")
    new_messages: list[dict[str, Any]] | None = Field(None, alias="newMessages", description="New top-level messages since the cursor.")
    new_replies: list[dict[str, Any]] | None = Field(None, alias="newReplies", description="New thread replies since the cursor, across all threads in the channel.")
    new_reactions: list[dict[str, Any]] | None = Field(None, alias="newReactions", description="New reactions since the cursor.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
    delivery: dict[str, Any] | None = Field(None, alias="delivery", description="")
    preview: str | None = Field(None, alias="preview", description="")
    scope: dict[str, Any] | None = Field(None, alias="scope", description="")
    recovery: dict[str, Any] | None = Field(None, alias="recovery", description="")

    @model_serializer(mode="wrap")
    def _serialize_response(self, handler, info):
        data = handler(self)
        for name, field in type(self).model_fields.items():
            if name not in self.model_fields_set:
                key = field.alias if info.by_alias and field.alias else name
                data.pop(key, None)
        return data
