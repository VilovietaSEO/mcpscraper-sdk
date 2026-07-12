from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class VideoFrameAnalysisStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    run_id: str = Field(..., alias="runId", description="The runId returned by video_frame_analysis.")


class VideoFrameAnalysisStatusOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    run_id: Any = Field(..., alias="runId", description="")
    status: Any = Field(..., alias="status", description="")
    progress: Any | None = Field(None, alias="progress", description="")
    frame_count: Any | None = Field(None, alias="frameCount", description="")
    artifact_path: Any = Field(..., alias="artifactPath", description="")
    report: Any = Field(..., alias="report", description="")
    error: Any = Field(..., alias="error", description="")
    reconciliation: Any | None = Field(None, alias="reconciliation", description="")
