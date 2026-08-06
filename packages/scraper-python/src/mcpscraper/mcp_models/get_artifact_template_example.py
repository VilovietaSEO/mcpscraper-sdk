from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GetArtifactTemplateExampleInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    preset_key: Literal['editorial_reading_room_v1', 'personal_authority_v1', 'newsroom_publisher_v1'] = Field(..., alias="presetKey", description="")


class GetArtifactTemplateExampleOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    example: dict[str, Any] | None = Field(None, alias="example", description="")
    error: str | None = Field(None, alias="error", description="")
    error_code: Literal['invalid_request', 'not_found', 'conflict', 'template_archived', 'renderer_unavailable', 'artifact_unavailable', 'view_link_unavailable', 'internal_error'] | None = Field(None, alias="errorCode", description="")
    request_id: str | None = Field(None, alias="requestId", description="")
