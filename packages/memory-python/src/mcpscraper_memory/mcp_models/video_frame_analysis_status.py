from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class VideoFrameAnalysisStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    run_id: Annotated[str, Field(min_length=1)] = Field(..., alias='runId', description='The runId returned by video_frame_analysis.')


VideoFrameAnalysisStatusOutputVariant1ProgressVariant1 = TypedDict('VideoFrameAnalysisStatusOutputVariant1ProgressVariant1', {
    'analyzed': Required[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)]],
    'total': Required[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)]],
})
VideoFrameAnalysisStatusOutputVariant1ProgressVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


VideoFrameAnalysisStatusOutputVariant1ReconciliationVariant1 = TypedDict('VideoFrameAnalysisStatusOutputVariant1ReconciliationVariant1', {
    'billedMc': Required[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)]],
    'refundedMc': Required[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)]],
    'effectiveFrames': Required[Union[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)], None]],
})
VideoFrameAnalysisStatusOutputVariant1ReconciliationVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class VideoFrameAnalysisStatusOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    run_id: Union[str, None] = Field(..., alias='runId', description='')
    status: Union[str, None] = Field(..., alias='status', description='')
    progress: Union[Union[VideoFrameAnalysisStatusOutputVariant1ProgressVariant1, None], None] = Field(None, alias='progress', description='')
    frame_count: Union[Union[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)], None], None] = Field(None, alias='frameCount', description='')
    artifact_path: Union[str, None] = Field(..., alias='artifactPath', description='')
    report: Union[str, None] = Field(..., alias='report', description='')
    error: Union[str, None] = Field(..., alias='error', description='')
    reconciliation: Union[Union[VideoFrameAnalysisStatusOutputVariant1ReconciliationVariant1, None], None] = Field(None, alias='reconciliation', description='')


VideoFrameAnalysisStatusOutputVariant2DeliveryArtifactsItem = TypedDict('VideoFrameAnalysisStatusOutputVariant2DeliveryArtifactsItem', {
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
VideoFrameAnalysisStatusOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


VideoFrameAnalysisStatusOutputVariant2DeliveryAvailableExportsItem = TypedDict('VideoFrameAnalysisStatusOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
VideoFrameAnalysisStatusOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


VideoFrameAnalysisStatusOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('VideoFrameAnalysisStatusOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
VideoFrameAnalysisStatusOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


VideoFrameAnalysisStatusOutputVariant2Delivery = TypedDict('VideoFrameAnalysisStatusOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[VideoFrameAnalysisStatusOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[VideoFrameAnalysisStatusOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[VideoFrameAnalysisStatusOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
VideoFrameAnalysisStatusOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


VideoFrameAnalysisStatusOutputVariant2RecoveryOperation = TypedDict('VideoFrameAnalysisStatusOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
VideoFrameAnalysisStatusOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


VideoFrameAnalysisStatusOutputVariant2Recovery = TypedDict('VideoFrameAnalysisStatusOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[VideoFrameAnalysisStatusOutputVariant2RecoveryOperation],
})
VideoFrameAnalysisStatusOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class VideoFrameAnalysisStatusOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: VideoFrameAnalysisStatusOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: VideoFrameAnalysisStatusOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(VideoFrameAnalysisStatusOutput).
VideoFrameAnalysisStatusOutput = Union[VideoFrameAnalysisStatusOutputVariant1, VideoFrameAnalysisStatusOutputVariant2]

_VideoFrameAnalysisStatusInputAdapter = TypeAdapter(VideoFrameAnalysisStatusInput)
_VideoFrameAnalysisStatusOutputAdapter = TypeAdapter(VideoFrameAnalysisStatusOutput)