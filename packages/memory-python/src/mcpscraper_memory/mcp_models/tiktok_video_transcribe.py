from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class TiktokVideoTranscribeInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    url: str = Field(..., alias='url', description='Public TikTok video URL, including short tiktok.com/t/ links. Transcribes the video audio from a playback URL exposed in the page DOM.')
    language: Union[Literal['af', 'am', 'ar', 'as', 'az', 'ba', 'be', 'bg', 'bn', 'bo', 'br', 'bs', 'ca', 'cs', 'cy', 'da', 'de', 'el', 'en', 'es', 'et', 'eu', 'fa', 'fi', 'fo', 'fr', 'gl', 'gu', 'ha', 'haw', 'he', 'hi', 'hr', 'ht', 'hu', 'hy', 'id', 'is', 'it', 'ja', 'jw', 'ka', 'kk', 'km', 'kn', 'ko', 'la', 'lb', 'ln', 'lo', 'lt', 'lv', 'mg', 'mi', 'mk', 'ml', 'mn', 'mr', 'ms', 'mt', 'my', 'ne', 'nl', 'nn', 'no', 'oc', 'pa', 'pl', 'ps', 'pt', 'ro', 'ru', 'sa', 'sd', 'si', 'sk', 'sl', 'sn', 'so', 'sq', 'sr', 'su', 'sv', 'sw', 'ta', 'te', 'tg', 'th', 'tk', 'tl', 'tr', 'tt', 'uk', 'ur', 'uz', 'vi', 'yi', 'yo', 'zh'], None] = Field(None, alias='language', description='Speech language. Default en.')


TiktokVideoTranscribeOutputVariant1ChunksItem = TypedDict('TiktokVideoTranscribeOutputVariant1ChunksItem', {
    'startSec': Required[Union[float, int]],
    'endSec': Required[Union[float, int]],
    'text': Required[str],
})
TiktokVideoTranscribeOutputVariant1ChunksItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TiktokVideoTranscribeOutputVariant1TranscriptSignal = TypedDict('TiktokVideoTranscribeOutputVariant1TranscriptSignal', {
    'status': Required[Literal['speech_detected', 'low_speech_signal', 'empty']],
    'speechDetected': Required[bool],
    'confidence': Required[Literal['medium', 'low']],
    'basis': Required[Literal['transcript_word_count_and_timing']],
    'mediaDurationSec': Required[Union[Union[float, int], None]],
    'wordsPerMinute': Required[Union[Union[float, int], None]],
    'retryRecommended': Required[bool],
    'warnings': Required[list[str]],
})
TiktokVideoTranscribeOutputVariant1TranscriptSignal.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class TiktokVideoTranscribeOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    source_url: str = Field(..., alias='sourceUrl', description='')
    page_url: str = Field(..., alias='pageUrl', description='')
    video_id: str = Field(..., alias='videoId', description='')
    owner_name: Union[str, None] = Field(..., alias='ownerName', description='')
    title: Union[str, None] = Field(..., alias='title', description='')
    video_duration_sec: Union[Union[float, int], None] = Field(..., alias='videoDurationSec', description='')
    video_url: Union[str, None] = Field(..., alias='videoUrl', description='')
    transcript_source: Literal['speech_model', 'captions'] = Field(..., alias='transcriptSource', description='')
    word_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='wordCount', description='')
    chunk_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='chunkCount', description='')
    transcript_text: str = Field(..., alias='transcriptText', description='')
    chunks: list[TiktokVideoTranscribeOutputVariant1ChunksItem] = Field(..., alias='chunks', description='')
    transcript_signal: TiktokVideoTranscribeOutputVariant1TranscriptSignal = Field(..., alias='transcriptSignal', description='')


TiktokVideoTranscribeOutputVariant2DeliveryArtifactsItem = TypedDict('TiktokVideoTranscribeOutputVariant2DeliveryArtifactsItem', {
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
TiktokVideoTranscribeOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TiktokVideoTranscribeOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('TiktokVideoTranscribeOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
TiktokVideoTranscribeOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TiktokVideoTranscribeOutputVariant2Delivery = TypedDict('TiktokVideoTranscribeOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[TiktokVideoTranscribeOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[TiktokVideoTranscribeOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
TiktokVideoTranscribeOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TiktokVideoTranscribeOutputVariant2RecoveryOperation = TypedDict('TiktokVideoTranscribeOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
TiktokVideoTranscribeOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TiktokVideoTranscribeOutputVariant2Recovery = TypedDict('TiktokVideoTranscribeOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[TiktokVideoTranscribeOutputVariant2RecoveryOperation],
})
TiktokVideoTranscribeOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class TiktokVideoTranscribeOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: TiktokVideoTranscribeOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: TiktokVideoTranscribeOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(TiktokVideoTranscribeOutput).
TiktokVideoTranscribeOutput = Union[TiktokVideoTranscribeOutputVariant1, TiktokVideoTranscribeOutputVariant2]

_TiktokVideoTranscribeInputAdapter = TypeAdapter(TiktokVideoTranscribeInput)
_TiktokVideoTranscribeOutputAdapter = TypeAdapter(TiktokVideoTranscribeOutput)