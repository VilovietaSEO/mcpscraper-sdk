from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AssistantBulkSendInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    assistant_ref: str = Field(..., alias="assistantRef", description="Opaque assistant reference submitting the reviewed bulk send.")
    context_version_ref: str = Field(..., alias="contextVersionRef", description="Opaque immutable context-version reference reviewed for the audience and content.")
    selection_ref: str = Field(..., alias="selectionRef", description="Opaque saved recipient-selection reference; raw recipient lists are not accepted here.")
    audience_digest: str = Field(..., alias="audienceDigest", description="SHA-256 digest of the immutable reviewed recipient audience.")
    message_ref: str = Field(..., alias="messageRef", description="Opaque reviewed draft or message reference; bulk message bodies are not accepted inline.")
    max_recipients: int = Field(..., alias="maxRecipients", description="Hard recipient ceiling for this execution; it may narrow but never widen the reviewed audience.")
    approval_ref: str = Field(..., alias="approvalRef", description="Opaque approval reference bound to this exact audience, content, and spend review.")
    confirmation: str = Field(..., alias="confirmation", description="Typed destructive-action confirmation for the exact reviewed bulk send.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Stable retry identity for this exact bulk send; changed inputs require a new key and review.")


class AssistantBulkSendOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    receipt: Any | None = Field(None, alias="receipt", description="")
    resource_uri: str | None = Field(None, alias="resourceUri", description="")
    truncated: bool = Field(..., alias="truncated", description="")
    untrusted_content: bool = Field(..., alias="untrustedContent", description="")
    error: dict[str, Any] | None = Field(None, alias="error", description="")
