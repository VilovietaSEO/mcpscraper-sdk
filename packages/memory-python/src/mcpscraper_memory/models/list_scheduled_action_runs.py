from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ListScheduledActionRunsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    id: str = Field(..., alias="id", description="The scheduled action id, from create-scheduled-action or list-scheduled-actions.")
    limit: int | None = Field(None, alias="limit", description="Maximum number of runs to return, newest first. Defaults to 50.")


class ListScheduledActionRunsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the run history was read.")
    runs: list[dict[str, Any]] | None = Field(None, alias="runs", description="Run history, newest first.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
