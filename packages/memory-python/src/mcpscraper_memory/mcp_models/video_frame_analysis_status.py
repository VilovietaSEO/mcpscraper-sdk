from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class VideoFrameAnalysisStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    run_id: str = Field(..., alias="runId", description="The runId returned by video_frame_analysis.")


class VideoFrameAnalysisStatusOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
