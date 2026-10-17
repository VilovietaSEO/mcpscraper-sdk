from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class YoutubeHarvestInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    mode: Literal['search', 'channel'] = Field(..., alias='mode', description='Use search for topic/keyword requests. Use channel when the user provides @handle, channel ID, or channel URL.')
    query: Union[str, None] = Field(None, alias='query', description='Required when mode is search. The YouTube search topic in the user’s words.')
    channel_handle: Union[str, None] = Field(None, alias='channelHandle', description='YouTube channel handle, channel ID, or URL. Examples: @mkbhd, UC..., https://youtube.com/@mkbhd.')
    max_videos: Union[Annotated[int, Field(ge=1, le=500)], None] = Field(None, alias='maxVideos', description='Number of videos to return. Default 50, maximum 500.')


YoutubeHarvestOutputVariant1ChannelVariant1 = TypedDict('YoutubeHarvestOutputVariant1ChannelVariant1', {
    'title': Required[Union[str, None]],
    'subscriberCount': Required[Union[str, None]],
})
YoutubeHarvestOutputVariant1ChannelVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


YoutubeHarvestOutputVariant1VideosItem = TypedDict('YoutubeHarvestOutputVariant1VideosItem', {
    'videoId': Required[str],
    'title': Required[str],
    'channelName': Required[Union[str, None]],
    'views': Required[Union[str, None]],
    'duration': Required[Union[str, None]],
    'url': Required[Union[str, None]],
})
YoutubeHarvestOutputVariant1VideosItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class YoutubeHarvestOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    mode: str = Field(..., alias='mode', description='')
    video_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='videoCount', description='')
    channel: Union[YoutubeHarvestOutputVariant1ChannelVariant1, None] = Field(..., alias='channel', description='')
    videos: list[YoutubeHarvestOutputVariant1VideosItem] = Field(..., alias='videos', description='')


YoutubeHarvestOutputVariant2DeliveryArtifactsItem = TypedDict('YoutubeHarvestOutputVariant2DeliveryArtifactsItem', {
    'artifactId': Required[str],
    'filename': Required[str],
    'contentType': Required[str],
    'bytes': Required[Union[float, int]],
    'sha256': Required[str],
    'expiresAt': Required[str],
    'capabilities': Required[list[str]],
    'downloadUrl': Required[Union[str, None]],
    'downloadUrlExpiresAt': Required[Union[str, None]],
    'downloadState': Required[Literal['available', 'local', 'unavailable']],
})
YoutubeHarvestOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


YoutubeHarvestOutputVariant2DeliveryAvailableExportsItem = TypedDict('YoutubeHarvestOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
YoutubeHarvestOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


YoutubeHarvestOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('YoutubeHarvestOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
YoutubeHarvestOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


YoutubeHarvestOutputVariant2Delivery = TypedDict('YoutubeHarvestOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[YoutubeHarvestOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[YoutubeHarvestOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[YoutubeHarvestOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
YoutubeHarvestOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


YoutubeHarvestOutputVariant2RecoveryOperation = TypedDict('YoutubeHarvestOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
YoutubeHarvestOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


YoutubeHarvestOutputVariant2Recovery = TypedDict('YoutubeHarvestOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[YoutubeHarvestOutputVariant2RecoveryOperation],
})
YoutubeHarvestOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class YoutubeHarvestOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: YoutubeHarvestOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: YoutubeHarvestOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(YoutubeHarvestOutput).
YoutubeHarvestOutput = Union[YoutubeHarvestOutputVariant1, YoutubeHarvestOutputVariant2]

_YoutubeHarvestInputAdapter = TypeAdapter(YoutubeHarvestInput)
_YoutubeHarvestOutputAdapter = TypeAdapter(YoutubeHarvestOutput)