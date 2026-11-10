from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


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

    ok: bool | None = Field(None, alias="ok", description="Whether the browser-agent action succeeded.")
    tool: str | None = Field(None, alias="tool", description="")
    session_id: Any | None = Field(None, alias="session_id", description="Browser session id when the response is scoped to a session.")
    replay_id: Any | None = Field(None, alias="replay_id", description="Replay id when the response is scoped to a replay.")
    source_file_path: Any | None = Field(None, alias="source_file_path", description="")
    annotated_file_path: Any | None = Field(None, alias="annotated_file_path", description="")
    bytes: Any | None = Field(None, alias="bytes", description="")
    width: Any | None = Field(None, alias="width", description="")
    height: Any | None = Field(None, alias="height", description="")
    annotation_count: Any | None = Field(None, alias="annotation_count", description="")
    mime_type: Any | None = Field(None, alias="mime_type", description="")
    delivery: dict[str, Any] | None = Field(None, alias="delivery", description="")
    preview: str | None = Field(None, alias="preview", description="")
    scope: dict[str, Any] | None = Field(None, alias="scope", description="")
    recovery: dict[str, Any] | None = Field(None, alias="recovery", description="")

    @model_serializer(mode="wrap")
    def _serialize_response(self, handler, info):
        data = handler(self)
        for name, field in type(self).model_fields.items():
            if name not in self.model_fields_set:
                key = field.alias if info.by_alias and field.alias else name
                data.pop(key, None)
        return data
