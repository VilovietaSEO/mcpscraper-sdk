from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AssistantApprovalDecideInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    approval_ref: str = Field(..., alias="approvalRef", description="Opaque pending approval reference being decided.")
    command_ref: str = Field(..., alias="commandRef", description="Opaque command reference bound to the reviewed approval.")
    plan_digest: str = Field(..., alias="planDigest", description="SHA-256 digest of the immutable reviewed plan.")
    context_version_ref: str = Field(..., alias="contextVersionRef", description="Opaque immutable context-version reference used during review.")
    action_digest: str = Field(..., alias="actionDigest", description="SHA-256 digest of the exact reviewed action.")
    argument_digest: str = Field(..., alias="argumentDigest", description="SHA-256 digest of the exact reviewed action arguments.")
    audience_digest: Any | None = Field(None, alias="audienceDigest", description="SHA-256 digest of the reviewed audience, or null when no audience exists.")
    spend_limit: Any | None = Field(None, alias="spendLimit", description="Exact approved spend ceiling, or null when the action has no spend.")
    decision: Literal['approve', 'reject'] = Field(..., alias="decision", description="Owner decision for this exact immutable approval.")
    typed_confirmation: Any | None = Field(None, alias="typedConfirmation", description="Typed confirmation required by the approval policy, or null when policy does not require one.")
    decided_at: str = Field(..., alias="decidedAt", description="ISO 8601 timestamp when the owner made this decision.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Stable retry identity for this exact approval decision.")


class AssistantApprovalDecideOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    receipt: Any | None = Field(None, alias="receipt", description="")
    resource_uri: str | None = Field(None, alias="resourceUri", description="")
    truncated: bool = Field(..., alias="truncated", description="")
    untrusted_content: bool = Field(..., alias="untrustedContent", description="")
    error: dict[str, Any] | None = Field(None, alias="error", description="")
