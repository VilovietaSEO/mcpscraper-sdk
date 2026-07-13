from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class FacebookAdTranscribeInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    video_url: str = Field(..., alias="videoUrl", description="Direct Meta/Facebook CDN video URL from facebook_page_intel or meta_ad_creative_media. Use transient sources immediately. Do not pass a public post/reel/share URL—use facebook_video_transcribe for those.")


class FacebookAdTranscribeOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    video_url: str = Field(..., alias="videoUrl", description="")
    word_count: int = Field(..., alias="wordCount", description="")
    chunk_count: int = Field(..., alias="chunkCount", description="")
    duration_ms: Any = Field(..., alias="durationMs", description="")
    transcript_text: str = Field(..., alias="transcriptText", description="")
    chunks: list[dict[str, Any]] = Field(..., alias="chunks", description="")
    transcript_signal: dict[str, Any] = Field(..., alias="transcriptSignal", description="")
    resolved_inputs: dict[str, Any] = Field(..., alias="resolvedInputs", description="")
