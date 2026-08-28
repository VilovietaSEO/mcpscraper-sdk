from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AssistantCommandInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    assistant_ref: str = Field(..., alias="assistantRef", description="Opaque assistant reference that owns this command.")
    instruction: str = Field(..., alias="instruction", description="Exact user instruction preserved for server-side intent derivation, policy review, and later execution.")
    context_packet_refs: list[str] | None = Field(None, alias="contextPacketRefs", description="Opaque context-packet references to resolve into one immutable server-owned context version.")
    attachment_refs: list[str] | None = Field(None, alias="attachmentRefs", description="Opaque attachment references to include in server-side context assembly.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Stable retry identity for this exact command; reuse it only for an identical retry.")


class AssistantCommandOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    receipt: Any | None = Field(None, alias="receipt", description="")
    resource_uri: str | None = Field(None, alias="resourceUri", description="")
    truncated: bool = Field(..., alias="truncated", description="")
    untrusted_content: bool = Field(..., alias="untrustedContent", description="")
    error: dict[str, Any] | None = Field(None, alias="error", description="")
