from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class TwitterTweetTranscriptInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    url: Annotated[str, Field(min_length=1)] = Field(..., alias='url', description='Tweet URL of the video to transcribe (e.g. https://x.com/TheoVon/status/1916982720317821050).')


class TwitterTweetTranscriptOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    tool: str = Field(..., alias='tool', description='The tool that produced this result.')
    count: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='count', description='Number of records returned.')
    items: list[dict[str, Any]] = Field(..., alias='items', description='Returned records. A lookup of one thing returns a single record.')
    meta: Union[dict[str, Any], None] = Field(None, alias='meta', description='Values returned alongside the records, such as nextCursor for the next page, or totals.')
    charged_credits: Union[float, int] = Field(..., alias='chargedCredits', description='Credits charged for this call.')
    duration_ms: Union[Union[float, int], None] = Field(..., alias='durationMs', description='Time taken in milliseconds.')


TwitterTweetTranscriptOutputVariant2DeliveryArtifactsItem = TypedDict('TwitterTweetTranscriptOutputVariant2DeliveryArtifactsItem', {
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
TwitterTweetTranscriptOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TwitterTweetTranscriptOutputVariant2DeliveryAvailableExportsItem = TypedDict('TwitterTweetTranscriptOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
TwitterTweetTranscriptOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TwitterTweetTranscriptOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('TwitterTweetTranscriptOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
TwitterTweetTranscriptOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TwitterTweetTranscriptOutputVariant2Delivery = TypedDict('TwitterTweetTranscriptOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[TwitterTweetTranscriptOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[TwitterTweetTranscriptOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[TwitterTweetTranscriptOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
TwitterTweetTranscriptOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TwitterTweetTranscriptOutputVariant2RecoveryOperation = TypedDict('TwitterTweetTranscriptOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
TwitterTweetTranscriptOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TwitterTweetTranscriptOutputVariant2Recovery = TypedDict('TwitterTweetTranscriptOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[TwitterTweetTranscriptOutputVariant2RecoveryOperation],
})
TwitterTweetTranscriptOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class TwitterTweetTranscriptOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: TwitterTweetTranscriptOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: TwitterTweetTranscriptOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(TwitterTweetTranscriptOutput).
TwitterTweetTranscriptOutput = Union[TwitterTweetTranscriptOutputVariant1, TwitterTweetTranscriptOutputVariant2]

_TwitterTweetTranscriptInputAdapter = TypeAdapter(TwitterTweetTranscriptInput)
_TwitterTweetTranscriptOutputAdapter = TypeAdapter(TwitterTweetTranscriptOutput)