from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class YoutubeTranscribeInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    video_id: str | None = Field(None, alias="videoId", description="YouTube video ID, e.g. dQw4w9WgXcQ. Use only an ID returned by youtube_harvest or visible in a YouTube URL; do not invent one.")
    url: str | None = Field(None, alias="url", description="Full YouTube URL. Use when the user pasted a URL instead of an ID. Provide videoId or url.")


class YoutubeTranscribeOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
