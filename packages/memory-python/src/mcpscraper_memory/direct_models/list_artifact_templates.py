from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ListArtifactTemplatesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="")
    session_id: str | None = Field(None, alias="sessionId", description="")
    status: Literal['active', 'archived', 'all'] | None = Field(None, alias="status", description="")
    query: str | None = Field(None, alias="query", description="")
    preset_key: Literal['editorial_reading_room_v1', 'personal_authority_v1', 'personal_authority_v2', 'newsroom_publisher_v1', 'blog_article_v1'] | None = Field(None, alias="presetKey", description="")


class ListArtifactTemplatesOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    presets: list[Any] | None = Field(None, alias="presets", description="")
    templates: list[dict[str, Any]] | None = Field(None, alias="templates", description="")
    error: str | None = Field(None, alias="error", description="")
    error_code: Literal['invalid_request', 'not_found', 'conflict', 'template_archived', 'renderer_unavailable', 'artifact_unavailable', 'view_link_unavailable', 'internal_error'] | None = Field(None, alias="errorCode", description="")
    request_id: str | None = Field(None, alias="requestId", description="")
