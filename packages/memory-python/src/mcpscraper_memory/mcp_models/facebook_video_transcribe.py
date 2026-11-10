from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class FacebookVideoTranscribeInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="Public Facebook reel/video/watch/post/share URL from facebook.com, m.facebook.com, or fb.watch. For connected account ads, get the correct public candidate from meta_ad_creative_media instead of guessing URL structure.")
    quality: Literal['best', 'hd', 'sd'] | None = Field(None, alias="quality", description="Preferred progressive MP4 quality. Use best by default; hd prefers the highest HD progressive URL; sd forces the SD URL.")


class FacebookVideoTranscribeOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    source_url: str | None = Field(None, alias="sourceUrl", description="")
    page_url: str | None = Field(None, alias="pageUrl", description="")
    video_id: Any | None = Field(None, alias="videoId", description="")
    owner_name: Any | None = Field(None, alias="ownerName", description="")
    selected_quality: str | None = Field(None, alias="selectedQuality", description="")
    bitrate: Any | None = Field(None, alias="bitrate", description="")
    video_duration_sec: Any | None = Field(None, alias="videoDurationSec", description="")
    video_url: str | None = Field(None, alias="videoUrl", description="")
    word_count: int | None = Field(None, alias="wordCount", description="")
    chunk_count: int | None = Field(None, alias="chunkCount", description="")
    transcript_text: str | None = Field(None, alias="transcriptText", description="")
    chunks: list[dict[str, Any]] | None = Field(None, alias="chunks", description="")
    transcript_signal: dict[str, Any] | None = Field(None, alias="transcriptSignal", description="")
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
