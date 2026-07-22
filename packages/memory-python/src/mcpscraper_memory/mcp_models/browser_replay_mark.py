from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class BrowserReplayMarkInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    session_id: str = Field(..., alias="session_id", description="The session id returned by browser_open or browser_list_sessions. A replay must already be recording.")
    target: dict[str, Any] = Field(..., alias="target", description="The exact DOM element or text range to mark in the current viewport.")
    type: Literal["box", "circle", "underline", "arrow"] | None = Field(None, alias="type", description="Annotation style to generate.")
    label: str | None = Field(None, alias="label", description="Optional callout text to render near the target.")
    color: str | None = Field(None, alias="color", description="Annotation color as hex, e.g. #ff3b30.")
    thickness: float | None = Field(None, alias="thickness", description="Stroke thickness in pixels. Defaults to 5.")
    padding: float | None = Field(None, alias="padding", description="Pixels to expand the DOM bounds so the highlight does not touch the text edge.")
    start_offset_seconds: float | None = Field(None, alias="start_offset_seconds", description="Offset from the current replay time; negative appears just before the mark action.")
    duration_seconds: float | None = Field(None, alias="duration_seconds", description="How long the annotation should remain visible.")


class BrowserReplayMarkOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="Whether the browser-agent action succeeded.")
    tool: str = Field(..., alias="tool", description="")
    session_id: Any = Field(..., alias="session_id", description="Browser session id when the response is scoped to a session.")
    replay_id: Any = Field(..., alias="replay_id", description="Replay id when the response is scoped to a replay.")
    annotation: dict[str, Any] = Field(..., alias="annotation", description="")
    source_width: Any = Field(..., alias="source_width", description="")
    source_height: Any = Field(..., alias="source_height", description="")
    target: Any = Field(..., alias="target", description="")
    hint: str = Field(..., alias="hint", description="")
