from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class ArtifactDescribeInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    artifact_id: str = Field(..., alias="artifactId", description="Artifact ID returned by a completed MCP result. Access remains bound to this authenticated caller.")


class ArtifactDescribeOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    artifact_id: str | None = Field(None, alias="artifactId", description="")
    filename: str | None = Field(None, alias="filename", description="")
    content_type: str | None = Field(None, alias="contentType", description="")
    bytes: float | None = Field(None, alias="bytes", description="")
    sha256: str | None = Field(None, alias="sha256", description="")
    created_at: str | None = Field(None, alias="createdAt", description="")
    expires_at: str | None = Field(None, alias="expiresAt", description="")
    capabilities: list[str] | None = Field(None, alias="capabilities", description="")
    download_url: Any | None = Field(None, alias="downloadUrl", description="")
    download_url_expires_at: Any | None = Field(None, alias="downloadUrlExpiresAt", description="")
    download_state: Literal['available', 'local', 'unavailable'] | None = Field(None, alias="downloadState", description="")
    local_path: Any | None = Field(None, alias="localPath", description="")
    local_path_scope: Any | None = Field(None, alias="localPathScope", description="")
    next_action: str | None = Field(None, alias="nextAction", description="")
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
