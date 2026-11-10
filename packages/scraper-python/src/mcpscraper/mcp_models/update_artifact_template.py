from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class UpdateArtifactTemplateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    template_id: str = Field(..., alias="templateId", description="Opaque saved-template identifier returned by an artifact-template tool.")
    name: str | None = Field(None, alias="name", description="Human-readable name for the record being created or updated.")
    description: str | None = Field(None, alias="description", description="Human-readable summary that distinguishes this record from similarly named records.")
    config: Any | None = Field(None, alias="config", description="Validated renderer configuration for the new immutable template version; arbitrary code is rejected.")
    authoring_instructions: str | None = Field(None, alias="authoringInstructions", description="Presentation guidance for authors using this saved template; executable prompts or code are rejected.")


class UpdateArtifactTemplateOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    template: dict[str, Any] | None = Field(None, alias="template", description="")
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
