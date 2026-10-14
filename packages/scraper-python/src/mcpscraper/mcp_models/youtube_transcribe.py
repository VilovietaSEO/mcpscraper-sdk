from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class YoutubeTranscribeInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    video_id: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='videoId', description='YouTube video ID, e.g. dQw4w9WgXcQ. Use only an ID returned by youtube_harvest or visible in a YouTube URL; do not invent one.')
    url: Union[str, None] = Field(None, alias='url', description='Full YouTube URL. Use when the user pasted a URL instead of an ID. Provide videoId or url.')
    language: Union[Literal['af', 'am', 'ar', 'as', 'az', 'ba', 'be', 'bg', 'bn', 'bo', 'br', 'bs', 'ca', 'cs', 'cy', 'da', 'de', 'el', 'en', 'es', 'et', 'eu', 'fa', 'fi', 'fo', 'fr', 'gl', 'gu', 'ha', 'haw', 'he', 'hi', 'hr', 'ht', 'hu', 'hy', 'id', 'is', 'it', 'ja', 'jw', 'ka', 'kk', 'km', 'kn', 'ko', 'la', 'lb', 'ln', 'lo', 'lt', 'lv', 'mg', 'mi', 'mk', 'ml', 'mn', 'mr', 'ms', 'mt', 'my', 'ne', 'nl', 'nn', 'no', 'oc', 'pa', 'pl', 'ps', 'pt', 'ro', 'ru', 'sa', 'sd', 'si', 'sk', 'sl', 'sn', 'so', 'sq', 'sr', 'su', 'sv', 'sw', 'ta', 'te', 'tg', 'th', 'tk', 'tl', 'tr', 'tt', 'uk', 'ur', 'uz', 'vi', 'yi', 'yo', 'zh'], None] = Field(None, alias='language', description='ISO language code of the video\'s spoken audio, e.g. "es", "fr". Defaults to "en" — set this when the user says the video is not in English, to avoid a failed transcription.')


YoutubeTranscribeOutputVariant1ChunksItem = TypedDict('YoutubeTranscribeOutputVariant1ChunksItem', {
    'startSec': Required[Union[float, int]],
    'endSec': Required[Union[float, int]],
    'text': Required[str],
})
YoutubeTranscribeOutputVariant1ChunksItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


YoutubeTranscribeOutputVariant1ResolvedInputs = TypedDict('YoutubeTranscribeOutputVariant1ResolvedInputs', {
    'videoId': Required[Union[str, None]],
    'url': Required[Union[str, None]],
})
YoutubeTranscribeOutputVariant1ResolvedInputs.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class YoutubeTranscribeOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    video_id: Union[str, None] = Field(..., alias='videoId', description='')
    url: Union[str, None] = Field(..., alias='url', description='')
    word_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='wordCount', description='')
    chunk_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='chunkCount', description='')
    duration_ms: Union[Union[float, int], None] = Field(..., alias='durationMs', description='')
    transcript_text: str = Field(..., alias='transcriptText', description='')
    chunks: list[YoutubeTranscribeOutputVariant1ChunksItem] = Field(..., alias='chunks', description='')
    resolved_inputs: YoutubeTranscribeOutputVariant1ResolvedInputs = Field(..., alias='resolvedInputs', description='')


YoutubeTranscribeOutputVariant2DeliveryArtifactsItem = TypedDict('YoutubeTranscribeOutputVariant2DeliveryArtifactsItem', {
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
YoutubeTranscribeOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


YoutubeTranscribeOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('YoutubeTranscribeOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
YoutubeTranscribeOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


YoutubeTranscribeOutputVariant2Delivery = TypedDict('YoutubeTranscribeOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[YoutubeTranscribeOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[YoutubeTranscribeOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
YoutubeTranscribeOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


YoutubeTranscribeOutputVariant2RecoveryOperation = TypedDict('YoutubeTranscribeOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
YoutubeTranscribeOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


YoutubeTranscribeOutputVariant2Recovery = TypedDict('YoutubeTranscribeOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[YoutubeTranscribeOutputVariant2RecoveryOperation],
})
YoutubeTranscribeOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class YoutubeTranscribeOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: YoutubeTranscribeOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: YoutubeTranscribeOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(YoutubeTranscribeOutput).
YoutubeTranscribeOutput = Union[YoutubeTranscribeOutputVariant1, YoutubeTranscribeOutputVariant2]

_YoutubeTranscribeInputAdapter = TypeAdapter(YoutubeTranscribeInput)
_YoutubeTranscribeOutputAdapter = TypeAdapter(YoutubeTranscribeOutput)