from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CreateArtifactTemplateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="")
    session_id: str | None = Field(None, alias="sessionId", description="")
    preset_key: Literal['editorial_reading_room_v1', 'personal_authority_v1', 'personal_authority_v2', 'newsroom_publisher_v1', 'blog_article_v1'] = Field(..., alias="presetKey", description="")
    name: str = Field(..., alias="name", description="")
    description: str | None = Field(None, alias="description", description="")
    authoring_instructions: str = Field(..., alias="authoringInstructions", description="")
    config: Any = Field(..., alias="config", description="")


class CreateArtifactTemplateOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    template: dict[str, Any] | None = Field(None, alias="template", description="")
    error: str | None = Field(None, alias="error", description="")
    error_code: Literal['invalid_request', 'not_found', 'conflict', 'template_archived', 'renderer_unavailable', 'artifact_unavailable', 'view_link_unavailable', 'internal_error'] | None = Field(None, alias="errorCode", description="")
    request_id: str | None = Field(None, alias="requestId", description="")
