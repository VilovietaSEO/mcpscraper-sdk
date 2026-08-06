from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class UpdateArtifactTemplateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    template_id: str = Field(..., alias="templateId", description="")
    name: str | None = Field(None, alias="name", description="")
    description: str | None = Field(None, alias="description", description="")
    config: Any | None = Field(None, alias="config", description="")
    authoring_instructions: str | None = Field(None, alias="authoringInstructions", description="")


class UpdateArtifactTemplateOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    template: dict[str, Any] | None = Field(None, alias="template", description="")
    error: str | None = Field(None, alias="error", description="")
    error_code: Literal['invalid_request', 'not_found', 'conflict', 'template_archived', 'renderer_unavailable', 'artifact_unavailable', 'view_link_unavailable', 'internal_error'] | None = Field(None, alias="errorCode", description="")
    request_id: str | None = Field(None, alias="requestId", description="")
