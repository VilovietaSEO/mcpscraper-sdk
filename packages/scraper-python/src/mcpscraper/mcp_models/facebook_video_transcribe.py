from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class FacebookVideoTranscribeInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    url: str = Field(..., alias='url', description='Public Facebook reel/video/watch/post/share URL from facebook.com, m.facebook.com, or fb.watch. For connected account ads, get the correct public candidate from meta_ad_creative_media instead of guessing URL structure.')
    quality: Union[Literal['best', 'hd', 'sd'], None] = Field(None, alias='quality', description='Preferred progressive MP4 quality. Use best by default; hd prefers the highest HD progressive URL; sd forces the SD URL.')


FacebookVideoTranscribeOutputVariant1ChunksItem = TypedDict('FacebookVideoTranscribeOutputVariant1ChunksItem', {
    'startSec': Required[Union[float, int]],
    'endSec': Required[Union[float, int]],
    'text': Required[str],
})
FacebookVideoTranscribeOutputVariant1ChunksItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookVideoTranscribeOutputVariant1TranscriptSignal = TypedDict('FacebookVideoTranscribeOutputVariant1TranscriptSignal', {
    'status': Required[Literal['speech_detected', 'low_speech_signal', 'empty']],
    'speechDetected': Required[bool],
    'confidence': Required[Literal['medium', 'low']],
    'basis': Required[Literal['transcript_word_count_and_timing']],
    'mediaDurationSec': Required[Union[Union[float, int], None]],
    'wordsPerMinute': Required[Union[Union[float, int], None]],
    'retryRecommended': Required[bool],
    'warnings': Required[list[str]],
})
FacebookVideoTranscribeOutputVariant1TranscriptSignal.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class FacebookVideoTranscribeOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    source_url: str = Field(..., alias='sourceUrl', description='')
    page_url: str = Field(..., alias='pageUrl', description='')
    video_id: Union[str, None] = Field(..., alias='videoId', description='')
    owner_name: Union[str, None] = Field(..., alias='ownerName', description='')
    selected_quality: str = Field(..., alias='selectedQuality', description='')
    bitrate: Union[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)], None] = Field(..., alias='bitrate', description='')
    video_duration_sec: Union[Union[float, int], None] = Field(..., alias='videoDurationSec', description='')
    video_url: str = Field(..., alias='videoUrl', description='')
    word_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='wordCount', description='')
    chunk_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='chunkCount', description='')
    transcript_text: str = Field(..., alias='transcriptText', description='')
    chunks: list[FacebookVideoTranscribeOutputVariant1ChunksItem] = Field(..., alias='chunks', description='')
    transcript_signal: FacebookVideoTranscribeOutputVariant1TranscriptSignal = Field(..., alias='transcriptSignal', description='')


FacebookVideoTranscribeOutputVariant2DeliveryArtifactsItem = TypedDict('FacebookVideoTranscribeOutputVariant2DeliveryArtifactsItem', {
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
FacebookVideoTranscribeOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookVideoTranscribeOutputVariant2DeliveryAvailableExportsItem = TypedDict('FacebookVideoTranscribeOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
FacebookVideoTranscribeOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookVideoTranscribeOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('FacebookVideoTranscribeOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
FacebookVideoTranscribeOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookVideoTranscribeOutputVariant2Delivery = TypedDict('FacebookVideoTranscribeOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[FacebookVideoTranscribeOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[FacebookVideoTranscribeOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[FacebookVideoTranscribeOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
FacebookVideoTranscribeOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookVideoTranscribeOutputVariant2RecoveryOperation = TypedDict('FacebookVideoTranscribeOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
FacebookVideoTranscribeOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookVideoTranscribeOutputVariant2Recovery = TypedDict('FacebookVideoTranscribeOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[FacebookVideoTranscribeOutputVariant2RecoveryOperation],
})
FacebookVideoTranscribeOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class FacebookVideoTranscribeOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: FacebookVideoTranscribeOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: FacebookVideoTranscribeOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(FacebookVideoTranscribeOutput).
FacebookVideoTranscribeOutput = Union[FacebookVideoTranscribeOutputVariant1, FacebookVideoTranscribeOutputVariant2]

_FacebookVideoTranscribeInputAdapter = TypeAdapter(FacebookVideoTranscribeInput)
_FacebookVideoTranscribeOutputAdapter = TypeAdapter(FacebookVideoTranscribeOutput)