from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AssistantNumberPurchaseInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    candidate_ref: str = Field(..., alias="candidateRef", description="Opaque unexpired candidate reference returned by assistant_number_search.")
    connection_ref: str = Field(..., alias="connectionRef", description="Opaque phone connection reference used for the reviewed candidate.")
    assistant_ref: str = Field(..., alias="assistantRef", description="Opaque assistant reference that will own the purchased number.")
    endpoint_ref: str = Field(..., alias="endpointRef", description="Opaque channel-endpoint reference that will be assigned after verified purchase.")
    approval_ref: str = Field(..., alias="approvalRef", description="Opaque approval reference bound to this exact current quote and requirements.")
    requirements_accepted: bool = Field(..., alias="requirementsAccepted", description="Confirms the owner reviewed and accepted the current disclosed recurring price and registration requirements.")
    confirmation: str = Field(..., alias="confirmation", description="Typed cost-bearing external-write confirmation for this exact reviewed number.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Stable retry identity for this exact purchase; never change inputs while reusing it.")


class AssistantNumberPurchaseOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    receipt: Any | None = Field(None, alias="receipt", description="")
    resource_uri: str | None = Field(None, alias="resourceUri", description="")
    truncated: bool = Field(..., alias="truncated", description="")
    untrusted_content: bool = Field(..., alias="untrustedContent", description="")
    error: dict[str, Any] | None = Field(None, alias="error", description="")
