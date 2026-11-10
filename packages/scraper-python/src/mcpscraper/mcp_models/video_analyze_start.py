from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class VideoAnalyzeStartInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    source_url: str = Field(..., alias="sourceUrl", description="A YouTube, Facebook, Instagram, TikTok, or Vimeo URL, or a direct video file URL (.mp4/.webm/.mov/.gif). Maximum duration: 60 minutes.")
    interval_s: float | None = Field(None, alias="intervalS", description="Preferred seconds between sampled frames (1-30). Default 2. For long videos the interval is automatically widened so the whole video is covered within the frame budget. Lower = denser sampling where the video is short enough to allow it.")
    max_frames: int | None = Field(None, alias="maxFrames", description="Hard cap on frames analyzed (≤480). Default 120. Frames are spread across the whole duration; lowest sampling interval is 1 second, so short videos cannot use more frames than their length in seconds.")
    detail: Literal['fast', 'standard', 'deep'] | None = Field(None, alias="detail", description="Analysis depth. Default standard.")
    vault: str | None = Field(None, alias="vault", description="Vault to write the final breakdown note into. Default \"Library\". You must have write access.")


class VideoAnalyzeStartOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    run_id: str | None = Field(None, alias="runId", description="")
    poll: dict[str, Any] | None = Field(None, alias="poll", description="")
    error: str | None = Field(None, alias="error", description="")
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
