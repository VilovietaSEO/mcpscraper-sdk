from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class SlackSendMessageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_id: str = Field(..., alias="connectionId", description="A Slack connectionId from list_service_connections, with actionsEnabled true.")
    channel: str = Field(..., alias="channel", description="Slack channel ID to send to, e.g. \"C1234567890\". Get this from the connection's own read tools, not guessed.")
    text: str = Field(..., alias="text", description="Message text to send.")


class SlackSendMessageOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    result: Any | None = Field(None, alias="result", description="")
    error: Any = Field(..., alias="error", description="")
