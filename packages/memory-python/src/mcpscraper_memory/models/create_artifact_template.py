from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CreateArtifactTemplateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    preset_key: str = Field(..., alias="presetKey", description="")
    name: str = Field(..., alias="name", description="")
    description: str | None = Field(None, alias="description", description="")
    config: dict[str, Any] = Field(..., alias="config", description="")
    authoring_instructions: str = Field(..., alias="authoringInstructions", description="")


class CreateArtifactTemplateOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    template: dict[str, Any] | None = Field(None, alias="template", description="")
    error: str | None = Field(None, alias="error", description="")
    error_code: Literal["invalid_request", "not_found", "conflict", "template_archived", "renderer_unavailable", "artifact_unavailable", "view_link_unavailable", "internal_error"] | None = Field(None, alias="errorCode", description="")
    request_id: str | None = Field(None, alias="requestId", description="")
