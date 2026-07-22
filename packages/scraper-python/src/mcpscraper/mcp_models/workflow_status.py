from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class WorkflowStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    run_id: str = Field(..., alias="runId", description="Workflow run id returned by workflow_run, workflow_step, or workflow_status. Use only a returned runId; do not construct one yourself.")


class WorkflowStatusOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    run: dict[str, Any] | None = Field(None, alias="run", description="")
    artifacts: list[dict[str, Any]] = Field(..., alias="artifacts", description="")
