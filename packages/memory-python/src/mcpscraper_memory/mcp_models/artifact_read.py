from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class ArtifactReadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    artifact_id: str = Field(..., alias="artifactId", description="Artifact ID returned by a completed MCP result. Access remains bound to this authenticated caller.")
    offset: int | None = Field(None, alias="offset", description="UTF-8 byte offset; use the exact nextOffset from the previous read.")
    max_bytes: int | None = Field(None, alias="maxBytes", description="Requested maximum bytes. The common serialized response budget may return a smaller window; follow nextOffset until null for the complete file.")


class ArtifactReadOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    artifact_id: str | None = Field(None, alias="artifactId", description="")
    text: str | None = Field(None, alias="text", description="")
    total_bytes: float | None = Field(None, alias="totalBytes", description="")
    offset: float | None = Field(None, alias="offset", description="")
    consumed_bytes: float | None = Field(None, alias="consumedBytes", description="")
    next_offset: Any | None = Field(None, alias="nextOffset", description="")
    content_type: str | None = Field(None, alias="contentType", description="")
    sha256: Any | None = Field(None, alias="sha256", description="")
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
