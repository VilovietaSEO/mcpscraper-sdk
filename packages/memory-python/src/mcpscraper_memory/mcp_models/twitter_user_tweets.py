from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class TwitterUserTweetsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    cursor: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='cursor', description="Opaque pagination cursor from a previous response's nextCursor. Omit for the first page.")
    handle: Annotated[str, Field(min_length=1)] = Field(..., alias='handle', description='Twitter/X handle without the leading @.')
    limit: Union[Annotated[int, Field(ge=1, le=100)], None] = Field(None, alias='limit', description='Page size to ask for (1-100, default 20). A page is never trimmed after the call, so follow nextCursor and pass it back as cursor to continue exactly where this response ended.')


class TwitterUserTweetsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    tool: str = Field(..., alias='tool', description='The tool that produced this result.')
    count: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='count', description='Number of records returned.')
    items: list[dict[str, Any]] = Field(..., alias='items', description='Returned records. A lookup of one thing returns a single record.')
    meta: Union[dict[str, Any], None] = Field(None, alias='meta', description='Values returned alongside the records, such as nextCursor for the next page, or totals.')
    charged_credits: Union[float, int] = Field(..., alias='chargedCredits', description='Credits charged for this call.')
    duration_ms: Union[Union[float, int], None] = Field(..., alias='durationMs', description='Time taken in milliseconds.')


TwitterUserTweetsOutputVariant2DeliveryArtifactsItem = TypedDict('TwitterUserTweetsOutputVariant2DeliveryArtifactsItem', {
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
TwitterUserTweetsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TwitterUserTweetsOutputVariant2DeliveryAvailableExportsItem = TypedDict('TwitterUserTweetsOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
TwitterUserTweetsOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TwitterUserTweetsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('TwitterUserTweetsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
TwitterUserTweetsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TwitterUserTweetsOutputVariant2Delivery = TypedDict('TwitterUserTweetsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[TwitterUserTweetsOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[TwitterUserTweetsOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[TwitterUserTweetsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
TwitterUserTweetsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TwitterUserTweetsOutputVariant2RecoveryOperation = TypedDict('TwitterUserTweetsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
TwitterUserTweetsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TwitterUserTweetsOutputVariant2Recovery = TypedDict('TwitterUserTweetsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[TwitterUserTweetsOutputVariant2RecoveryOperation],
})
TwitterUserTweetsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class TwitterUserTweetsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: TwitterUserTweetsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: TwitterUserTweetsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(TwitterUserTweetsOutput).
TwitterUserTweetsOutput = Union[TwitterUserTweetsOutputVariant1, TwitterUserTweetsOutputVariant2]

_TwitterUserTweetsInputAdapter = TypeAdapter(TwitterUserTweetsInput)
_TwitterUserTweetsOutputAdapter = TypeAdapter(TwitterUserTweetsOutput)