from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class ReportArtifactReadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    artifact_id: str = Field(..., alias="artifactId", description="Artifact id returned inline by a tool whose result was too large to inline. Use only a returned artifactId; do not construct one yourself.")
    offset: int | None = Field(None, alias="offset", description="Byte offset to start reading from. Pass the previous call's nextOffset to continue.")
    max_bytes: int | None = Field(None, alias="maxBytes", description="Maximum bytes of artifact text to return in this window.")


class ReportArtifactReadOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    artifact_id: str | None = Field(None, alias="artifactId", description="")
    text: str | None = Field(None, alias="text", description="")
    total_bytes: int | None = Field(None, alias="totalBytes", description="")
    next_offset: Any | None = Field(None, alias="nextOffset", description="")
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
