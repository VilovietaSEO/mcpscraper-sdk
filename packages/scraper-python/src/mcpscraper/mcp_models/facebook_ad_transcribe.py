from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class FacebookAdTranscribeInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    video_url: str = Field(..., alias='videoUrl', description='Direct Meta/Facebook CDN video URL from facebook_page_intel or meta_ad_creative_media. Use transient sources immediately. Do not pass a public post/reel/share URL—use facebook_video_transcribe for those.')


FacebookAdTranscribeOutputVariant1ChunksItem = TypedDict('FacebookAdTranscribeOutputVariant1ChunksItem', {
    'startSec': Required[Union[float, int]],
    'endSec': Required[Union[float, int]],
    'text': Required[str],
})
FacebookAdTranscribeOutputVariant1ChunksItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookAdTranscribeOutputVariant1TranscriptSignal = TypedDict('FacebookAdTranscribeOutputVariant1TranscriptSignal', {
    'status': Required[Literal['speech_detected', 'low_speech_signal', 'empty']],
    'speechDetected': Required[bool],
    'confidence': Required[Literal['medium', 'low']],
    'basis': Required[Literal['transcript_word_count_and_timing']],
    'mediaDurationSec': Required[Union[Union[float, int], None]],
    'wordsPerMinute': Required[Union[Union[float, int], None]],
    'retryRecommended': Required[bool],
    'warnings': Required[list[str]],
})
FacebookAdTranscribeOutputVariant1TranscriptSignal.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookAdTranscribeOutputVariant1ResolvedInputs = TypedDict('FacebookAdTranscribeOutputVariant1ResolvedInputs', {
    'videoUrl': Required[str],
})
FacebookAdTranscribeOutputVariant1ResolvedInputs.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class FacebookAdTranscribeOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    video_url: str = Field(..., alias='videoUrl', description='')
    word_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='wordCount', description='')
    chunk_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='chunkCount', description='')
    duration_ms: Union[Union[float, int], None] = Field(..., alias='durationMs', description='')
    transcript_text: str = Field(..., alias='transcriptText', description='')
    chunks: list[FacebookAdTranscribeOutputVariant1ChunksItem] = Field(..., alias='chunks', description='')
    transcript_signal: FacebookAdTranscribeOutputVariant1TranscriptSignal = Field(..., alias='transcriptSignal', description='')
    resolved_inputs: FacebookAdTranscribeOutputVariant1ResolvedInputs = Field(..., alias='resolvedInputs', description='')


FacebookAdTranscribeOutputVariant2DeliveryArtifactsItem = TypedDict('FacebookAdTranscribeOutputVariant2DeliveryArtifactsItem', {
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
FacebookAdTranscribeOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookAdTranscribeOutputVariant2DeliveryAvailableExportsItem = TypedDict('FacebookAdTranscribeOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
FacebookAdTranscribeOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookAdTranscribeOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('FacebookAdTranscribeOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
FacebookAdTranscribeOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookAdTranscribeOutputVariant2Delivery = TypedDict('FacebookAdTranscribeOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[FacebookAdTranscribeOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[FacebookAdTranscribeOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[FacebookAdTranscribeOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
FacebookAdTranscribeOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookAdTranscribeOutputVariant2RecoveryOperation = TypedDict('FacebookAdTranscribeOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
FacebookAdTranscribeOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookAdTranscribeOutputVariant2Recovery = TypedDict('FacebookAdTranscribeOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[FacebookAdTranscribeOutputVariant2RecoveryOperation],
})
FacebookAdTranscribeOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class FacebookAdTranscribeOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: FacebookAdTranscribeOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: FacebookAdTranscribeOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(FacebookAdTranscribeOutput).
FacebookAdTranscribeOutput = Union[FacebookAdTranscribeOutputVariant1, FacebookAdTranscribeOutputVariant2]

_FacebookAdTranscribeInputAdapter = TypeAdapter(FacebookAdTranscribeInput)
_FacebookAdTranscribeOutputAdapter = TypeAdapter(FacebookAdTranscribeOutput)