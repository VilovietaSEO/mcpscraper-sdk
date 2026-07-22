from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GoogleAdsTranscribeInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    video_url: str = Field(..., alias="videoUrl", description="Direct googlevideo.com playback URL from google_ads_page_intel. For YouTube-hosted ads use youtube_transcribe instead.")


class GoogleAdsTranscribeOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    video_url: str = Field(..., alias="videoUrl", description="")
    word_count: int = Field(..., alias="wordCount", description="")
    chunk_count: int = Field(..., alias="chunkCount", description="")
    duration_ms: Any = Field(..., alias="durationMs", description="")
    transcript_text: str = Field(..., alias="transcriptText", description="")
    chunks: list[dict[str, Any]] = Field(..., alias="chunks", description="")
    resolved_inputs: dict[str, Any] = Field(..., alias="resolvedInputs", description="")
