from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class VideoFrameAnalysisInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    source_url: str = Field(..., alias="sourceUrl", description="A YouTube, Facebook, Instagram, TikTok, or Vimeo URL (downloaded automatically), or a direct video file URL (.mp4/.webm/.mov). Videos up to 60 minutes are supported.")
    interval_s: float | None = Field(None, alias="intervalS", description="Preferred seconds between sampled frames (1-30, default 2). Automatically widened for long videos so the whole duration is covered within the frame budget.")
    max_frames: int | None = Field(None, alias="maxFrames", description="Max frames analyzed (<=480, default 120). Reserves the number of 120-frame tiers requested; unused tiers are refunded. Analysis-model usage is billed separately. Frames are spread evenly across the whole video, with at least 1 second between frames.")
    detail: Literal['fast', 'standard', 'deep'] | None = Field(None, alias="detail", description="Analysis depth. Default standard.")
    vault: str | None = Field(None, alias="vault", description="Memory vault to save the finished breakdown into. Default \"Library\".")


class VideoFrameAnalysisOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    run_id: Any | None = Field(None, alias="runId", description="")
    status: Any | None = Field(None, alias="status", description="")
    message: Any | None = Field(None, alias="message", description="")
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
