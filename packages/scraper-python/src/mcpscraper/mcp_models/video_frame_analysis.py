from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class VideoFrameAnalysisInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    source_url: str = Field(..., alias="sourceUrl", description="A YouTube, Facebook, Instagram, TikTok, or Vimeo URL (downloaded automatically), or a direct video file URL (.mp4/.webm/.mov). Videos up to 30 minutes are supported.")
    interval_s: float | None = Field(None, alias="intervalS", description="Preferred seconds between sampled frames (1-30, default 2). Automatically widened for long videos so the whole duration is covered within the frame budget.")
    max_frames: int | None = Field(None, alias="maxFrames", description="Max frames analyzed (<=480, default 120). $1 per 120 frames requested — 120=$1 … 480=$4 — automatically refunded down if the video cannot use them (minimum 1s between frames). Frames are spread evenly across the whole video.")
    detail: Literal["fast", "standard", "deep"] | None = Field(None, alias="detail", description="Analysis depth. Default standard.")
    vault: str | None = Field(None, alias="vault", description="Memory vault to save the finished breakdown into. Default \"Library\".")


class VideoFrameAnalysisOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    run_id: Any = Field(..., alias="runId", description="")
    status: Any = Field(..., alias="status", description="")
    message: Any = Field(..., alias="message", description="")
