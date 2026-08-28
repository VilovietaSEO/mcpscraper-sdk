from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AssistantApprovalsListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    state: Literal['pending', 'approved', 'rejected', 'expired', 'cancelled'] | None = Field(None, alias="state", description="Optional approval-state filter; omit to return all caller-owned approval states.")
    cursor: str | None = Field(None, alias="cursor", description="Opaque continuation cursor returned by the previous approval page.")
    page_size: int | None = Field(None, alias="pageSize", description="Maximum approvals to return in this bounded page.")


class AssistantApprovalsListOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    receipt: Any | None = Field(None, alias="receipt", description="")
    resource_uri: str | None = Field(None, alias="resourceUri", description="")
    truncated: bool = Field(..., alias="truncated", description="")
    untrusted_content: bool = Field(..., alias="untrustedContent", description="")
    error: dict[str, Any] | None = Field(None, alias="error", description="")
