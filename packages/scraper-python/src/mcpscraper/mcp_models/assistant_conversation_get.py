from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AssistantConversationGetInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    conversation_ref: str = Field(..., alias="conversationRef", description="Opaque caller-owned conversation reference returned by assistant_status or another assistant read.")
    cursor: str | None = Field(None, alias="cursor", description="Opaque message cursor returned by the preceding page; omit for the newest page.")
    page_size: int | None = Field(None, alias="pageSize", description="Maximum messages to return in this bounded page.")


class AssistantConversationGetOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    receipt: Any | None = Field(None, alias="receipt", description="")
    resource_uri: str | None = Field(None, alias="resourceUri", description="")
    truncated: bool = Field(..., alias="truncated", description="")
    untrusted_content: bool = Field(..., alias="untrustedContent", description="")
    error: dict[str, Any] | None = Field(None, alias="error", description="")
