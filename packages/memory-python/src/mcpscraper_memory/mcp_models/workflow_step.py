from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class WorkflowStepInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    run_id: str = Field(..., alias="runId", description="Workflow run id returned by workflow_run/workflow_step/workflow_status. Advances the run by exactly one step.")


class WorkflowStepOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    run_id: str = Field(..., alias="runId", description="")
    run: dict[str, Any] | None = Field(None, alias="run", description="")
    summary: Any | None = Field(None, alias="summary", description="")
    step: dict[str, Any] | None = Field(None, alias="step", description="")
    next_step: Any | None = Field(None, alias="nextStep", description="")
    done: bool = Field(..., alias="done", description="")
    artifacts: list[dict[str, Any]] = Field(..., alias="artifacts", description="")
