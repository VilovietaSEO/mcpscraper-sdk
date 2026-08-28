from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AssistantGrantCreateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    grant_ref: str = Field(..., alias="grantRef", description="Caller-generated opaque grant reference for this immutable revision.")
    assistant_ref: str = Field(..., alias="assistantRef", description="Opaque assistant reference receiving the grant.")
    revision: int = Field(..., alias="revision", description="Positive immutable grant revision; changed authority requires a new revision.")
    operation: Literal['assistant.message.draft', 'assistant.message.send', 'assistant.bulk.prepare', 'assistant.bulk.send', 'assistant.conversation.get', 'assistant.conversation.list', 'assistant.execution.status', 'gmail_search_messages', 'gmail_get_message', 'gmail_get_attachment', 'calendar.event.draft', 'zoom.meeting.draft', 'browser_read', 'browser_goto'] = Field(..., alias="operation", description="Exact operation authorized by this grant; grants never authorize an operation not named here.")
    authority_class: Literal['observe', 'draft', 'reversible_action', 'external_write', 'destructive'] = Field(..., alias="authorityClass", description="Maximum authority class permitted for the exact operation.")
    approval_mode: Literal['deny', 'per_occurrence', 'per_recipient', 'preauthorized', 'typed_confirmation'] = Field(..., alias="approvalMode", description="Approval rule applied after this grant; destructive grants require typed confirmation.")
    scope: dict[str, Any] = Field(..., alias="scope", description="Closed authority scope; omitted account, browser-profile, vault, audience, occurrence, and spend fields remain unavailable.")
    starts_at: str = Field(..., alias="startsAt", description="ISO 8601 start of this immutable grant revision.")
    expires_at: str = Field(..., alias="expiresAt", description="ISO 8601 expiry; it must be later than startsAt.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Stable retry identity for creating this exact grant revision.")


class AssistantGrantCreateOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    receipt: Any | None = Field(None, alias="receipt", description="")
    resource_uri: str | None = Field(None, alias="resourceUri", description="")
    truncated: bool = Field(..., alias="truncated", description="")
    untrusted_content: bool = Field(..., alias="untrustedContent", description="")
    error: dict[str, Any] | None = Field(None, alias="error", description="")
