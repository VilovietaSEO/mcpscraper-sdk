from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class GetArtifactTemplateExampleInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    preset_key: Literal['editorial_reading_room_v1', 'personal_authority_v1', 'personal_authority_v2', 'newsroom_publisher_v1', 'blog_article_v1'] = Field(..., alias="presetKey", description="Registered preset key returned by list_artifact_templates.")


class GetArtifactTemplateExampleOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    example: dict[str, Any] | None = Field(None, alias="example", description="")
    error: str | None = Field(None, alias="error", description="")
    error_code: Literal['invalid_request', 'not_found', 'conflict', 'template_archived', 'renderer_unavailable', 'artifact_unavailable', 'internal_error'] | None = Field(None, alias="errorCode", description="")
    request_id: str | None = Field(None, alias="requestId", description="")
    delivery: dict[str, Any] | None = Field(None, alias="delivery", description="")
    preview: str | None = Field(None, alias="preview", description="")
    scope: dict[str, Any] | None = Field(None, alias="scope", description="")
    recovery: dict[str, Any] | None = Field(None, alias="recovery", description="")

    @model_serializer(mode="wrap")
    def _serialize_response(self, handler, info):
        data = handler(self)
        for name, field in type(self).model_fields.items():
            if name not in self.model_fields_set:
                key = field.alias if info.by_alias and field.alias else name
                data.pop(key, None)
        return data
