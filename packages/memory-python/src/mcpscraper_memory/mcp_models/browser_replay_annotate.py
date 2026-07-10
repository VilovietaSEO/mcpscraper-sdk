from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class BrowserReplayAnnotateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    session_id: str = Field(..., alias="session_id", description="The session id returned by browser_open or browser_list_sessions.")
    replay_id: str = Field(..., alias="replay_id", description="The replay id returned by browser_replay_start or browser_list_replays.")
    annotations: list[dict[str, Any]] = Field(..., alias="annotations", description="Timed overlay annotations. Prefer ones from browser_replay_mark; otherwise use exact DOM bounds from browser_locate.")
    filename: str | None = Field(None, alias="filename", description="Optional output MP4 filename. Defaults to a timestamped filename.")
    source_width: float | None = Field(None, alias="source_width", description="Width of the screenshot coordinate space used for annotations. Defaults to the replay video width.")
    source_height: float | None = Field(None, alias="source_height", description="Height of the annotation coordinate space; if smaller than the replay video height, the browser chrome offset is inferred.")
    source_left_offset: float | None = Field(None, alias="source_left_offset", description="Explicit X offset from annotation to replay video coordinates. Usually omitted.")
    source_top_offset: float | None = Field(None, alias="source_top_offset", description="Explicit Y offset from annotation to replay video coordinates. Usually omitted.")


class BrowserReplayAnnotateOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
