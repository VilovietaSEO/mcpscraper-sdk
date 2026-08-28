from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AssistantGrantRevokeInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    grant_ref: str = Field(..., alias="grantRef", description="Opaque active grant reference to revoke.")
    operation: Literal['assistant.message.draft', 'assistant.message.send', 'assistant.bulk.prepare', 'assistant.bulk.send', 'assistant.conversation.get', 'assistant.conversation.list', 'assistant.execution.status', 'gmail_search_messages', 'gmail_get_message', 'gmail_get_attachment', 'calendar.event.draft', 'zoom.meeting.draft', 'browser_read', 'browser_goto'] = Field(..., alias="operation", description="Exact operation named by the grant being revoked.")
    reason: str = Field(..., alias="reason", description="Owner-facing reason recorded for the revocation.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Stable retry identity for revoking this exact grant.")


class AssistantGrantRevokeOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    receipt: Any | None = Field(None, alias="receipt", description="")
    resource_uri: str | None = Field(None, alias="resourceUri", description="")
    truncated: bool = Field(..., alias="truncated", description="")
    untrusted_content: bool = Field(..., alias="untrustedContent", description="")
    error: dict[str, Any] | None = Field(None, alias="error", description="")
