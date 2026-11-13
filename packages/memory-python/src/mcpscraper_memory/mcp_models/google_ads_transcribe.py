from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class GoogleAdsTranscribeInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    video_url: str = Field(..., alias='videoUrl', description='Direct googlevideo.com playback URL from google_ads_page_intel. For YouTube-hosted ads use youtube_transcribe instead.')


GoogleAdsTranscribeOutputVariant1ChunksItem = TypedDict('GoogleAdsTranscribeOutputVariant1ChunksItem', {
    'startSec': Required[Union[float, int]],
    'endSec': Required[Union[float, int]],
    'text': Required[str],
})
GoogleAdsTranscribeOutputVariant1ChunksItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GoogleAdsTranscribeOutputVariant1ResolvedInputs = TypedDict('GoogleAdsTranscribeOutputVariant1ResolvedInputs', {
    'videoUrl': Required[str],
})
GoogleAdsTranscribeOutputVariant1ResolvedInputs.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GoogleAdsTranscribeOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    video_url: str = Field(..., alias='videoUrl', description='')
    word_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='wordCount', description='')
    chunk_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='chunkCount', description='')
    duration_ms: Union[Union[float, int], None] = Field(..., alias='durationMs', description='')
    transcript_text: str = Field(..., alias='transcriptText', description='')
    chunks: list[GoogleAdsTranscribeOutputVariant1ChunksItem] = Field(..., alias='chunks', description='')
    resolved_inputs: GoogleAdsTranscribeOutputVariant1ResolvedInputs = Field(..., alias='resolvedInputs', description='')


GoogleAdsTranscribeOutputVariant2DeliveryArtifactsItem = TypedDict('GoogleAdsTranscribeOutputVariant2DeliveryArtifactsItem', {
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
GoogleAdsTranscribeOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GoogleAdsTranscribeOutputVariant2DeliveryAvailableExportsItem = TypedDict('GoogleAdsTranscribeOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
GoogleAdsTranscribeOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GoogleAdsTranscribeOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GoogleAdsTranscribeOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GoogleAdsTranscribeOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GoogleAdsTranscribeOutputVariant2Delivery = TypedDict('GoogleAdsTranscribeOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GoogleAdsTranscribeOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[GoogleAdsTranscribeOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GoogleAdsTranscribeOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GoogleAdsTranscribeOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GoogleAdsTranscribeOutputVariant2RecoveryOperation = TypedDict('GoogleAdsTranscribeOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GoogleAdsTranscribeOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GoogleAdsTranscribeOutputVariant2Recovery = TypedDict('GoogleAdsTranscribeOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GoogleAdsTranscribeOutputVariant2RecoveryOperation],
})
GoogleAdsTranscribeOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GoogleAdsTranscribeOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GoogleAdsTranscribeOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GoogleAdsTranscribeOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GoogleAdsTranscribeOutput).
GoogleAdsTranscribeOutput = Union[GoogleAdsTranscribeOutputVariant1, GoogleAdsTranscribeOutputVariant2]

_GoogleAdsTranscribeInputAdapter = TypeAdapter(GoogleAdsTranscribeInput)
_GoogleAdsTranscribeOutputAdapter = TypeAdapter(GoogleAdsTranscribeOutput)