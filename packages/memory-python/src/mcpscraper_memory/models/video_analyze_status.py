from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class VideoAnalyzeStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    run_id: str = Field(..., alias="runId", description="The runId returned by video-analyze-start.")


class VideoAnalyzeStatusOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    status: str | None = Field(None, alias="status", description="")
    progress: dict[str, Any] | None = Field(None, alias="progress", description="")
    frame_count: float | None = Field(None, alias="frameCount", description="")
    max_frames: float | None = Field(None, alias="maxFrames", description="")
    cost_usd: float | None = Field(None, alias="costUsd", description="")
    artifact_path: str | None = Field(None, alias="artifactPath", description="")
    report: str | None = Field(None, alias="report", description="")
    error: str | None = Field(None, alias="error", description="")
