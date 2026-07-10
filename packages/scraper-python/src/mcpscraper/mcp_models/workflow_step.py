from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class WorkflowStepInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    run_id: str = Field(..., alias="runId", description="Workflow run id returned by workflow_run/workflow_step/workflow_status. Advances the run by exactly one step.")


class WorkflowStepOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
