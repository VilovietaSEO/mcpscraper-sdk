from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmPipelineListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")


class CrmPipelineListOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    pipelines: list[dict[str, Any]] | None = Field(None, alias="pipelines", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
