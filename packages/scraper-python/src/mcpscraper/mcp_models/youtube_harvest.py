from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class YoutubeHarvestInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    mode: Literal["search", "channel"] = Field(..., alias="mode", description="Use search for topic/keyword requests. Use channel when the user provides @handle, channel ID, or channel URL.")
    query: str | None = Field(None, alias="query", description="Required when mode is search. The YouTube search topic in the user’s words.")
    channel_handle: str | None = Field(None, alias="channelHandle", description="YouTube channel handle, channel ID, or URL. Examples: @mkbhd, UC..., https://youtube.com/@mkbhd.")
    max_videos: int | None = Field(None, alias="maxVideos", description="Number of videos to return. Default 50, maximum 500.")


class YoutubeHarvestOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    mode: str = Field(..., alias="mode", description="")
    video_count: int = Field(..., alias="videoCount", description="")
    channel: Any = Field(..., alias="channel", description="")
    videos: list[dict[str, Any]] = Field(..., alias="videos", description="")
