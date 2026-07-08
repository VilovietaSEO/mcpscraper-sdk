from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class VideoAnalyzeStartInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key (Bearer secret). Optional when the MCP session is already authenticated.")
    session_id: str | None = Field(None, alias="sessionId", description="Session identifier. Optional; defaults to the current MCP session.")
    source_url: str = Field(..., alias="sourceUrl", description="Direct URL to the video file (.mp4/.webm/.mov/.gif).")
    interval_s: float | None = Field(None, alias="intervalS", description="Preferred seconds between sampled frames (1-30). Default 2. For long videos the interval is automatically widened so the whole video is covered within the frame budget. Lower = denser sampling where the video is short enough to allow it.")
    max_frames: int | None = Field(None, alias="maxFrames", description="Hard cap on frames analyzed (≤480). Default 120. Frames are spread across the whole duration; lowest sampling interval is 1 second, so short videos cannot use more frames than their length in seconds.")
    detail: Literal["fast", "standard", "deep"] | None = Field(None, alias="detail", description="Analysis depth. Default standard.")
    vault: str | None = Field(None, alias="vault", description="Vault to write the final breakdown note into. Default \"Library\". You must have write access.")


class VideoAnalyzeStartOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    run_id: str | None = Field(None, alias="runId", description="")
    poll: dict[str, Any] | None = Field(None, alias="poll", description="")
    error: str | None = Field(None, alias="error", description="")
