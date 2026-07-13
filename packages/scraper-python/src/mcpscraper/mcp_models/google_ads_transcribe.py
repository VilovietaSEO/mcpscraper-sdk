from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GoogleAdsTranscribeInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    video_url: str = Field(..., alias="videoUrl", description="Direct googlevideo.com playback URL from google_ads_page_intel. For YouTube-hosted ads use youtube_transcribe instead.")


class GoogleAdsTranscribeOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
