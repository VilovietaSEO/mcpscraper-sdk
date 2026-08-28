from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AssistantExecutionStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    execution_ref: str = Field(..., alias="executionRef", description="Opaque caller-owned execution reference returned by an accepted command.")
    command_ref: str | None = Field(None, alias="commandRef", description="Optional opaque command reference used to include its bounded action receipts.")


class AssistantExecutionStatusOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    receipt: Any | None = Field(None, alias="receipt", description="")
    resource_uri: str | None = Field(None, alias="resourceUri", description="")
    truncated: bool = Field(..., alias="truncated", description="")
    untrusted_content: bool = Field(..., alias="untrustedContent", description="")
    error: dict[str, Any] | None = Field(None, alias="error", description="")
