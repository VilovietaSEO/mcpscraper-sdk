from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class YoutubeHarvestInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    mode: Literal['search', 'channel'] = Field(..., alias="mode", description="Use search for topic/keyword requests. Use channel when the user provides @handle, channel ID, or channel URL.")
    query: str | None = Field(None, alias="query", description="Required when mode is search. The YouTube search topic in the user’s words.")
    channel_handle: str | None = Field(None, alias="channelHandle", description="YouTube channel handle, channel ID, or URL. Examples: @mkbhd, UC..., https://youtube.com/@mkbhd.")
    max_videos: int | None = Field(None, alias="maxVideos", description="Number of videos to return. Default 50, maximum 500.")


class YoutubeHarvestOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    mode: str | None = Field(None, alias="mode", description="")
    video_count: int | None = Field(None, alias="videoCount", description="")
    channel: Any | None = Field(None, alias="channel", description="")
    videos: list[dict[str, Any]] | None = Field(None, alias="videos", description="")
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
