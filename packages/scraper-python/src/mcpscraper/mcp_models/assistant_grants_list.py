from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AssistantGrantsListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    assistant_ref: str | None = Field(None, alias="assistantRef", description="Optional opaque assistant reference used to narrow the caller-owned grants.")
    cursor: str | None = Field(None, alias="cursor", description="Opaque continuation cursor returned by the previous grant page.")
    page_size: int | None = Field(None, alias="pageSize", description="Maximum grants to return in this bounded page.")


class AssistantGrantsListOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    receipt: Any | None = Field(None, alias="receipt", description="")
    resource_uri: str | None = Field(None, alias="resourceUri", description="")
    truncated: bool = Field(..., alias="truncated", description="")
    untrusted_content: bool = Field(..., alias="untrustedContent", description="")
    error: dict[str, Any] | None = Field(None, alias="error", description="")
