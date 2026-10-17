from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class VideoAnalyzeStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    run_id: str = Field(..., alias='runId', description='The runId returned by video-analyze-start.')


VideoAnalyzeStatusOutputVariant1Progress = TypedDict('VideoAnalyzeStatusOutputVariant1Progress', {
    'analyzed': Required[Union[float, int]],
    'total': Required[Union[float, int]],
})
VideoAnalyzeStatusOutputVariant1Progress.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class VideoAnalyzeStatusOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    status: Union[str, None] = Field(None, alias='status', description='')
    progress: Union[VideoAnalyzeStatusOutputVariant1Progress, None] = Field(None, alias='progress', description='')
    frame_count: Union[Union[float, int], None] = Field(None, alias='frameCount', description='')
    max_frames: Union[Union[float, int], None] = Field(None, alias='maxFrames', description='')
    cost_usd: Union[Union[float, int], None] = Field(None, alias='costUsd', description='')
    artifact_path: Union[str, None] = Field(None, alias='artifactPath', description='')
    report: Union[str, None] = Field(None, alias='report', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


VideoAnalyzeStatusOutputVariant2DeliveryArtifactsItem = TypedDict('VideoAnalyzeStatusOutputVariant2DeliveryArtifactsItem', {
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
VideoAnalyzeStatusOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


VideoAnalyzeStatusOutputVariant2DeliveryAvailableExportsItem = TypedDict('VideoAnalyzeStatusOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
VideoAnalyzeStatusOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


VideoAnalyzeStatusOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('VideoAnalyzeStatusOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
VideoAnalyzeStatusOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


VideoAnalyzeStatusOutputVariant2Delivery = TypedDict('VideoAnalyzeStatusOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[VideoAnalyzeStatusOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[VideoAnalyzeStatusOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[VideoAnalyzeStatusOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
VideoAnalyzeStatusOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


VideoAnalyzeStatusOutputVariant2RecoveryOperation = TypedDict('VideoAnalyzeStatusOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
VideoAnalyzeStatusOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


VideoAnalyzeStatusOutputVariant2Recovery = TypedDict('VideoAnalyzeStatusOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[VideoAnalyzeStatusOutputVariant2RecoveryOperation],
})
VideoAnalyzeStatusOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class VideoAnalyzeStatusOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: VideoAnalyzeStatusOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: VideoAnalyzeStatusOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(VideoAnalyzeStatusOutput).
VideoAnalyzeStatusOutput = Union[VideoAnalyzeStatusOutputVariant2, VideoAnalyzeStatusOutputVariant1]

_VideoAnalyzeStatusInputAdapter = TypeAdapter(VideoAnalyzeStatusInput)
_VideoAnalyzeStatusOutputAdapter = TypeAdapter(VideoAnalyzeStatusOutput)