from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class InstagramReelTranscriptInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    url: Annotated[str, Field(min_length=1)] = Field(..., alias='url', description='The URL of a public Instagram reel or video post (e.g. https://www.instagram.com/reel/C8yKXdRxKqK/), or an Instagram CDN media URL you already hold.')
    word_timestamps: Union[bool, None] = Field(None, alias='wordTimestamps', description='Set true to include a precise timestamp for every word in the transcript (e.g. true).')


class InstagramReelTranscriptOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    tool: str = Field(..., alias='tool', description='The tool that produced this result.')
    count: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='count', description='Number of records returned.')
    items: list[dict[str, Any]] = Field(..., alias='items', description='Returned records. A lookup of one thing returns a single record.')
    meta: Union[dict[str, Any], None] = Field(None, alias='meta', description='Values returned alongside the records, such as nextCursor for the next page, or totals.')
    charged_credits: Union[float, int] = Field(..., alias='chargedCredits', description='Credits charged for this call.')
    duration_ms: Union[Union[float, int], None] = Field(..., alias='durationMs', description='Time taken in milliseconds.')


InstagramReelTranscriptOutputVariant2DeliveryArtifactsItem = TypedDict('InstagramReelTranscriptOutputVariant2DeliveryArtifactsItem', {
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
InstagramReelTranscriptOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramReelTranscriptOutputVariant2DeliveryAvailableExportsItem = TypedDict('InstagramReelTranscriptOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
InstagramReelTranscriptOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramReelTranscriptOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('InstagramReelTranscriptOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
InstagramReelTranscriptOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramReelTranscriptOutputVariant2Delivery = TypedDict('InstagramReelTranscriptOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[InstagramReelTranscriptOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[InstagramReelTranscriptOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[InstagramReelTranscriptOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
InstagramReelTranscriptOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramReelTranscriptOutputVariant2RecoveryOperation = TypedDict('InstagramReelTranscriptOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
InstagramReelTranscriptOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramReelTranscriptOutputVariant2Recovery = TypedDict('InstagramReelTranscriptOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[InstagramReelTranscriptOutputVariant2RecoveryOperation],
})
InstagramReelTranscriptOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class InstagramReelTranscriptOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: InstagramReelTranscriptOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: InstagramReelTranscriptOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(InstagramReelTranscriptOutput).
InstagramReelTranscriptOutput = Union[InstagramReelTranscriptOutputVariant1, InstagramReelTranscriptOutputVariant2]

_InstagramReelTranscriptInputAdapter = TypeAdapter(InstagramReelTranscriptInput)
_InstagramReelTranscriptOutputAdapter = TypeAdapter(InstagramReelTranscriptOutput)