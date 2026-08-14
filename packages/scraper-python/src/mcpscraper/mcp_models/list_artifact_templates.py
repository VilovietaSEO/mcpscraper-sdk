from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ListArtifactTemplatesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    status: Literal['active', 'archived', 'all'] | None = Field(None, alias="status", description="Lifecycle status used to filter or update the selected records.")
    query: str | None = Field(None, alias="query", description="Optional case-insensitive search text for preset and saved-template names, descriptions, renderer keys, and authoring guidance.")
    preset_key: Literal['editorial_reading_room_v1', 'personal_authority_v1', 'personal_authority_v2', 'newsroom_publisher_v1', 'blog_article_v1'] | None = Field(None, alias="presetKey", description="Optional renderer-family filter. Saved templates are matched through their current immutable version.")


class ListArtifactTemplatesOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    presets: list[dict[str, Any]] | None = Field(None, alias="presets", description="")
    templates: list[dict[str, Any]] | None = Field(None, alias="templates", description="")
    error: str | None = Field(None, alias="error", description="")
    error_code: Literal['invalid_request', 'not_found', 'conflict', 'template_archived', 'renderer_unavailable', 'artifact_unavailable', 'view_link_unavailable', 'internal_error'] | None = Field(None, alias="errorCode", description="")
    request_id: str | None = Field(None, alias="requestId", description="")
