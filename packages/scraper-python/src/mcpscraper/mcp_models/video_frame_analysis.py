from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class VideoFrameAnalysisInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    source_url: Annotated[str, Field(min_length=1)] = Field(..., alias='sourceUrl', description='A YouTube, Facebook, Instagram, TikTok, or Vimeo URL (downloaded automatically), or a direct video file URL (.mp4/.webm/.mov). Videos up to 60 minutes are supported.')
    interval_s: Union[Annotated[Union[float, int], Field(ge=1, le=30)], None] = Field(None, alias='intervalS', description='Preferred seconds between sampled frames (1-30, default 2). Automatically widened for long videos so the whole duration is covered within the frame budget.')
    max_frames: Union[Annotated[int, Field(ge=1, le=480)], None] = Field(None, alias='maxFrames', description='Max frames analyzed (<=480, default 120). Reserves the number of 120-frame tiers requested; unused tiers are refunded. Analysis-model usage is billed separately. Frames are spread evenly across the whole video, with at least 1 second between frames.')
    detail: Union[Literal['fast', 'standard', 'deep'], None] = Field(None, alias='detail', description='Analysis depth. Default standard.')
    vault: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='vault', description='Memory vault to save the finished breakdown into. Default "Library".')


class VideoFrameAnalysisOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    run_id: Union[str, None] = Field(..., alias='runId', description='')
    status: Union[str, None] = Field(..., alias='status', description='')
    message: Union[str, None] = Field(..., alias='message', description='')


VideoFrameAnalysisOutputVariant2DeliveryArtifactsItem = TypedDict('VideoFrameAnalysisOutputVariant2DeliveryArtifactsItem', {
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
VideoFrameAnalysisOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


VideoFrameAnalysisOutputVariant2DeliveryAvailableExportsItem = TypedDict('VideoFrameAnalysisOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
VideoFrameAnalysisOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


VideoFrameAnalysisOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('VideoFrameAnalysisOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
VideoFrameAnalysisOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


VideoFrameAnalysisOutputVariant2Delivery = TypedDict('VideoFrameAnalysisOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[VideoFrameAnalysisOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[VideoFrameAnalysisOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[VideoFrameAnalysisOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
VideoFrameAnalysisOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


VideoFrameAnalysisOutputVariant2RecoveryOperation = TypedDict('VideoFrameAnalysisOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
VideoFrameAnalysisOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


VideoFrameAnalysisOutputVariant2Recovery = TypedDict('VideoFrameAnalysisOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[VideoFrameAnalysisOutputVariant2RecoveryOperation],
})
VideoFrameAnalysisOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class VideoFrameAnalysisOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: VideoFrameAnalysisOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: VideoFrameAnalysisOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(VideoFrameAnalysisOutput).
VideoFrameAnalysisOutput = Union[VideoFrameAnalysisOutputVariant1, VideoFrameAnalysisOutputVariant2]

_VideoFrameAnalysisInputAdapter = TypeAdapter(VideoFrameAnalysisInput)
_VideoFrameAnalysisOutputAdapter = TypeAdapter(VideoFrameAnalysisOutput)