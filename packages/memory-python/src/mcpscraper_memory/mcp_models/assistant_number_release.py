from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AssistantNumberReleaseInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    number_ref: str = Field(..., alias="numberRef", description="Opaque caller-owned number reference to release.")
    approval_ref: str = Field(..., alias="approvalRef", description="Opaque approval reference bound to releasing this exact number.")
    reason: str = Field(..., alias="reason", description="Owner-facing release reason stored with the destructive receipt.")
    confirmation: str = Field(..., alias="confirmation", description="Typed destructive confirmation; releasing a number can break replies and may be irreversible.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Stable retry identity for releasing this exact number.")


class AssistantNumberReleaseOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    receipt: Any | None = Field(None, alias="receipt", description="")
    resource_uri: str | None = Field(None, alias="resourceUri", description="")
    truncated: bool = Field(..., alias="truncated", description="")
    untrusted_content: bool = Field(..., alias="untrustedContent", description="")
    error: dict[str, Any] | None = Field(None, alias="error", description="")
