from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class CrmPipelineUpsertInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP transport already authenticated this request.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional MCP session identifier used for active account context.")
    pipeline_id: str | None = Field(None, alias="pipelineId", description="Existing owner-scoped pipeline UUID; omit to create a pipeline.")
    label: str = Field(..., alias="label", description="Human-readable pipeline label.")
    base_version: int = Field(..., alias="baseVersion", description="Expected pipeline version for concurrency control; use 0 only when creating.")
    is_default: bool | None = Field(None, alias="isDefault", description="Whether this should become the owner default pipeline.")
    stages: list[dict[str, Any]] = Field(..., alias="stages", description="Complete ordered stage definition for the pipeline.")


class CrmPipelineUpsertOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    message: str = Field(..., alias="message", description="")
    pipeline: dict[str, Any] | None = Field(None, alias="pipeline", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
