from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GmailGetMessageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_id: str = Field(..., alias="connectionId", description="The same tenant-owned Gmail connectionId used to discover this message.")
    message_id: str = Field(..., alias="messageId", description="One Gmail messageId returned by gmail_search_messages or a frozen selection preview.")
    include_raw_artifact: bool | None = Field(None, alias="includeRawArtifact", description="Keep true when complete RFC 822 fidelity or later export is required; large content is returned through an owned artifact, never silently truncated.")


class GmailGetMessageOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    message: dict[str, Any] | None = Field(None, alias="message", description="")
    error: Any = Field(..., alias="error", description="")
