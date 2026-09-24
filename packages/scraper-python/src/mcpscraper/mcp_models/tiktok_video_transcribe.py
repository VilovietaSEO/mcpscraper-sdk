from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class TiktokVideoTranscribeInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="Public TikTok video URL, including short tiktok.com/t/ links. Transcribes the video audio from a playback URL exposed in the page DOM.")
    language: Literal['af', 'am', 'ar', 'as', 'az', 'ba', 'be', 'bg', 'bn', 'bo', 'br', 'bs', 'ca', 'cs', 'cy', 'da', 'de', 'el', 'en', 'es', 'et', 'eu', 'fa', 'fi', 'fo', 'fr', 'gl', 'gu', 'ha', 'haw', 'he', 'hi', 'hr', 'ht', 'hu', 'hy', 'id', 'is', 'it', 'ja', 'jw', 'ka', 'kk', 'km', 'kn', 'ko', 'la', 'lb', 'ln', 'lo', 'lt', 'lv', 'mg', 'mi', 'mk', 'ml', 'mn', 'mr', 'ms', 'mt', 'my', 'ne', 'nl', 'nn', 'no', 'oc', 'pa', 'pl', 'ps', 'pt', 'ro', 'ru', 'sa', 'sd', 'si', 'sk', 'sl', 'sn', 'so', 'sq', 'sr', 'su', 'sv', 'sw', 'ta', 'te', 'tg', 'th', 'tk', 'tl', 'tr', 'tt', 'uk', 'ur', 'uz', 'vi', 'yi', 'yo', 'zh'] | None = Field(None, alias="language", description="Speech language. Default en.")


class TiktokVideoTranscribeOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    source_url: str = Field(..., alias="sourceUrl", description="")
    page_url: str = Field(..., alias="pageUrl", description="")
    video_id: str = Field(..., alias="videoId", description="")
    owner_name: Any = Field(..., alias="ownerName", description="")
    title: Any = Field(..., alias="title", description="")
    video_duration_sec: Any = Field(..., alias="videoDurationSec", description="")
    video_url: Any = Field(..., alias="videoUrl", description="")
    transcript_source: Literal['speech_model', 'captions'] = Field(..., alias="transcriptSource", description="")
    word_count: int = Field(..., alias="wordCount", description="")
    chunk_count: int = Field(..., alias="chunkCount", description="")
    transcript_text: str = Field(..., alias="transcriptText", description="")
    chunks: list[dict[str, Any]] = Field(..., alias="chunks", description="")
    transcript_signal: dict[str, Any] = Field(..., alias="transcriptSignal", description="")
