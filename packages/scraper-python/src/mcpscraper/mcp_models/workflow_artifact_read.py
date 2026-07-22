from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class WorkflowArtifactReadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    run_id: str = Field(..., alias="runId", description="Workflow run id returned by workflow_run, workflow_step, or workflow_status. Use only a returned runId; do not construct one yourself.")
    artifact_id: str = Field(..., alias="artifactId", description="Artifact id from the run artifact list returned by workflow_run, workflow_step, or workflow_status. Use only a returned artifactId; do not construct one yourself.")
    max_bytes: int | None = Field(None, alias="maxBytes", description="Maximum bytes of artifact text to return inline.")


class WorkflowArtifactReadOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    run_id: str = Field(..., alias="runId", description="")
    artifact_id: str = Field(..., alias="artifactId", description="")
    content_type: str = Field(..., alias="contentType", description="")
    bytes: int = Field(..., alias="bytes", description="")
    truncated: bool = Field(..., alias="truncated", description="")
    text: str = Field(..., alias="text", description="")
