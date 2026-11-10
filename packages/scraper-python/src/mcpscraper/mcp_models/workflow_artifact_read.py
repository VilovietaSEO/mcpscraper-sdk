from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class WorkflowArtifactReadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    run_id: str = Field(..., alias="runId", description="Workflow run id returned by workflow_run, workflow_step, or workflow_status. Use only a returned runId; do not construct one yourself.")
    artifact_id: str = Field(..., alias="artifactId", description="Artifact id from the run artifact list returned by workflow_run, workflow_step, or workflow_status. Use only a returned artifactId; do not construct one yourself.")
    max_bytes: int | None = Field(None, alias="maxBytes", description="Maximum bytes of artifact text to return inline.")


class WorkflowArtifactReadOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    run_id: str | None = Field(None, alias="runId", description="")
    artifact_id: str | None = Field(None, alias="artifactId", description="")
    content_type: str | None = Field(None, alias="contentType", description="")
    bytes: int | None = Field(None, alias="bytes", description="")
    truncated: bool | None = Field(None, alias="truncated", description="")
    text: str | None = Field(None, alias="text", description="")
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
