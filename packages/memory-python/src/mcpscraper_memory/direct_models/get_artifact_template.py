from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GetArtifactTemplateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="")
    session_id: str | None = Field(None, alias="sessionId", description="")
    template_id: str = Field(..., alias="templateId", description="")


class GetArtifactTemplateOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
