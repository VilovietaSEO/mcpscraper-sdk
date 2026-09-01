from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class UpdateArtifactTemplateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="")
    session_id: str | None = Field(None, alias="sessionId", description="")
    template_id: str = Field(..., alias="templateId", description="")
    name: str | None = Field(None, alias="name", description="")
    description: str | None = Field(None, alias="description", description="")
    config: Any | None = Field(None, alias="config", description="")
    authoring_instructions: str | None = Field(None, alias="authoringInstructions", description="")


class UpdateArtifactTemplateOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
