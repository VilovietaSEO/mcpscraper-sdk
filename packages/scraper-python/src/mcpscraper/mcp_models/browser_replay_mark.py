from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class BrowserReplayMarkInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    session_id: str = Field(..., alias="session_id", description="The session id returned by browser_open or browser_list_sessions. A replay must already be recording.")
    target: dict[str, Any] = Field(..., alias="target", description="The exact DOM element or text range to mark in the current viewport.")
    type: Literal['box', 'circle', 'underline', 'arrow'] | None = Field(None, alias="type", description="Annotation style to generate.")
    label: str | None = Field(None, alias="label", description="Optional callout text to render near the target.")
    color: str | None = Field(None, alias="color", description="Annotation color as hex, e.g. #ff3b30.")
    thickness: float | None = Field(None, alias="thickness", description="Stroke thickness in pixels. Defaults to 5.")
    padding: float | None = Field(None, alias="padding", description="Pixels to expand the DOM bounds so the highlight does not touch the text edge.")
    start_offset_seconds: float | None = Field(None, alias="start_offset_seconds", description="Offset from the current replay time; negative appears just before the mark action.")
    duration_seconds: float | None = Field(None, alias="duration_seconds", description="How long the annotation should remain visible.")


class BrowserReplayMarkOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="Whether the browser-agent action succeeded.")
    tool: str | None = Field(None, alias="tool", description="")
    session_id: Any | None = Field(None, alias="session_id", description="Browser session id when the response is scoped to a session.")
    replay_id: Any | None = Field(None, alias="replay_id", description="Replay id when the response is scoped to a replay.")
    annotation: dict[str, Any] | None = Field(None, alias="annotation", description="")
    source_width: Any | None = Field(None, alias="source_width", description="")
    source_height: Any | None = Field(None, alias="source_height", description="")
    target: Any | None = Field(None, alias="target", description="")
    hint: str | None = Field(None, alias="hint", description="")
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
