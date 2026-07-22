from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class WorkflowRunInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    workflow_id: Literal["directory", "get-leads", "agent-packet", "local-competitive-audit", "map-comparison", "serp-comparison", "paa-expansion-brief", "ai-overview-language"] = Field(..., alias="workflowId", description="Workflow to run. Call workflow_list or workflow_suggest first when unsure.")
    input: dict[str, Any] | None = Field(None, alias="input", description="Workflow-specific input object; shape depends on workflowId. Call workflow_list or workflow_suggest to see required fields.")
    webhook_url: str | None = Field(None, alias="webhookUrl", description="Optional HTTPS webhook to receive the completed hosted workflow run event.")


class WorkflowRunOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    workflow_id: str = Field(..., alias="workflowId", description="")
    input: dict[str, Any] = Field(..., alias="input", description="")
    run: dict[str, Any] | None = Field(None, alias="run", description="")
    summary: dict[str, Any] | None = Field(None, alias="summary", description="")
    step: dict[str, Any] | None = Field(None, alias="step", description="")
    next_step: Any | None = Field(None, alias="nextStep", description="")
    done: bool | None = Field(None, alias="done", description="")
    artifacts: list[dict[str, Any]] = Field(..., alias="artifacts", description="")
