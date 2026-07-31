from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CreateArtifactTemplateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="")
    session_id: str | None = Field(None, alias="sessionId", description="")
    preset_key: str = Field(..., alias="presetKey", description="")
    name: str = Field(..., alias="name", description="")
    description: str | None = Field(None, alias="description", description="")
    config: dict[str, Any] = Field(..., alias="config", description="")
    authoring_instructions: str = Field(..., alias="authoringInstructions", description="")


class CreateArtifactTemplateOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
