from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AssistantNumberStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    number_ref: str = Field(..., alias="numberRef", description="Opaque caller-owned number reference whose readiness should be read.")


class AssistantNumberStatusOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    receipt: Any | None = Field(None, alias="receipt", description="")
    resource_uri: str | None = Field(None, alias="resourceUri", description="")
    truncated: bool = Field(..., alias="truncated", description="")
    untrusted_content: bool = Field(..., alias="untrustedContent", description="")
    error: dict[str, Any] | None = Field(None, alias="error", description="")
