from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class GoogleAdsTranscribeInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    video_url: str = Field(..., alias="videoUrl", description="Direct googlevideo.com playback URL from google_ads_page_intel. For YouTube-hosted ads use youtube_transcribe instead.")


class GoogleAdsTranscribeOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    video_url: str | None = Field(None, alias="videoUrl", description="")
    word_count: int | None = Field(None, alias="wordCount", description="")
    chunk_count: int | None = Field(None, alias="chunkCount", description="")
    duration_ms: Any | None = Field(None, alias="durationMs", description="")
    transcript_text: str | None = Field(None, alias="transcriptText", description="")
    chunks: list[dict[str, Any]] | None = Field(None, alias="chunks", description="")
    resolved_inputs: dict[str, Any] | None = Field(None, alias="resolvedInputs", description="")
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
