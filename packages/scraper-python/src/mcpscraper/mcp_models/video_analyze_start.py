from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class VideoAnalyzeStartInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    source_url: str = Field(..., alias='sourceUrl', description='A YouTube, Facebook, Instagram, TikTok, or Vimeo URL (downloaded automatically), or a direct video file URL (.mp4/.webm/.mov/.gif).')
    interval_s: Union[Annotated[Union[float, int], Field(ge=1, le=30)], None] = Field(None, alias='intervalS', description='Preferred seconds between sampled frames (1-30). Default 2. For long videos the interval is automatically widened so the whole video is covered within the frame budget. Lower = denser sampling where the video is short enough to allow it.')
    max_frames: Union[Annotated[int, Field(ge=1, le=480)], None] = Field(None, alias='maxFrames', description='Hard cap on frames analyzed (≤480). Default 120. Frames are spread across the whole duration; lowest sampling interval is 1 second, so short videos cannot use more frames than their length in seconds.')
    detail: Union[Literal['fast', 'standard', 'deep'], None] = Field(None, alias='detail', description='Analysis depth. Default standard.')
    vault: Union[str, None] = Field(None, alias='vault', description='Vault to write the final breakdown note into. Default "Library". You must have write access.')


VideoAnalyzeStartOutputVariant1PollArgs = TypedDict('VideoAnalyzeStartOutputVariant1PollArgs', {
    'runId': Required[str],
})
VideoAnalyzeStartOutputVariant1PollArgs.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


VideoAnalyzeStartOutputVariant1Poll = TypedDict('VideoAnalyzeStartOutputVariant1Poll', {
    'tool': Required[str],
    'args': Required[VideoAnalyzeStartOutputVariant1PollArgs],
})
VideoAnalyzeStartOutputVariant1Poll.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class VideoAnalyzeStartOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    run_id: Union[str, None] = Field(None, alias='runId', description='')
    poll: Union[VideoAnalyzeStartOutputVariant1Poll, None] = Field(None, alias='poll', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


VideoAnalyzeStartOutputVariant2DeliveryArtifactsItem = TypedDict('VideoAnalyzeStartOutputVariant2DeliveryArtifactsItem', {
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
VideoAnalyzeStartOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


VideoAnalyzeStartOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('VideoAnalyzeStartOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
VideoAnalyzeStartOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


VideoAnalyzeStartOutputVariant2Delivery = TypedDict('VideoAnalyzeStartOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[VideoAnalyzeStartOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[VideoAnalyzeStartOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
VideoAnalyzeStartOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


VideoAnalyzeStartOutputVariant2RecoveryOperation = TypedDict('VideoAnalyzeStartOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
VideoAnalyzeStartOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


VideoAnalyzeStartOutputVariant2Recovery = TypedDict('VideoAnalyzeStartOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[VideoAnalyzeStartOutputVariant2RecoveryOperation],
})
VideoAnalyzeStartOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class VideoAnalyzeStartOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: VideoAnalyzeStartOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: VideoAnalyzeStartOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(VideoAnalyzeStartOutput).
VideoAnalyzeStartOutput = Union[VideoAnalyzeStartOutputVariant2, VideoAnalyzeStartOutputVariant1]

_VideoAnalyzeStartInputAdapter = TypeAdapter(VideoAnalyzeStartInput)
_VideoAnalyzeStartOutputAdapter = TypeAdapter(VideoAnalyzeStartOutput)