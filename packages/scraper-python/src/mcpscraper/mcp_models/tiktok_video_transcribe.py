from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class TiktokVideoTranscribeInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="Public TikTok video URL, including short tiktok.com/t/ links. Transcribes the video audio from a playback URL exposed in the page DOM.")
    language: Literal['af', 'am', 'ar', 'as', 'az', 'ba', 'be', 'bg', 'bn', 'bo', 'br', 'bs', 'ca', 'cs', 'cy', 'da', 'de', 'el', 'en', 'es', 'et', 'eu', 'fa', 'fi', 'fo', 'fr', 'gl', 'gu', 'ha', 'haw', 'he', 'hi', 'hr', 'ht', 'hu', 'hy', 'id', 'is', 'it', 'ja', 'jw', 'ka', 'kk', 'km', 'kn', 'ko', 'la', 'lb', 'ln', 'lo', 'lt', 'lv', 'mg', 'mi', 'mk', 'ml', 'mn', 'mr', 'ms', 'mt', 'my', 'ne', 'nl', 'nn', 'no', 'oc', 'pa', 'pl', 'ps', 'pt', 'ro', 'ru', 'sa', 'sd', 'si', 'sk', 'sl', 'sn', 'so', 'sq', 'sr', 'su', 'sv', 'sw', 'ta', 'te', 'tg', 'th', 'tk', 'tl', 'tr', 'tt', 'uk', 'ur', 'uz', 'vi', 'yi', 'yo', 'zh'] | None = Field(None, alias="language", description="Speech language. Default en.")


class TiktokVideoTranscribeOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    source_url: str | None = Field(None, alias="sourceUrl", description="")
    page_url: str | None = Field(None, alias="pageUrl", description="")
    video_id: str | None = Field(None, alias="videoId", description="")
    owner_name: Any | None = Field(None, alias="ownerName", description="")
    title: Any | None = Field(None, alias="title", description="")
    video_duration_sec: Any | None = Field(None, alias="videoDurationSec", description="")
    video_url: Any | None = Field(None, alias="videoUrl", description="")
    transcript_source: Literal['speech_model', 'captions'] | None = Field(None, alias="transcriptSource", description="")
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
