from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


CommonsSaveFilterInputFilter = TypedDict('CommonsSaveFilterInputFilter', {
    'mode': NotRequired[Literal['lexical', 'semantic', 'hybrid']],
    'query': NotRequired[Annotated[str, Field(max_length=300)]],
    'entityType': NotRequired[Annotated[str, Field(max_length=120)]],
    'tag': NotRequired[Annotated[str, Field(max_length=80)]],
    'tags': NotRequired[Annotated[list[Annotated[str, Field(min_length=1, max_length=80)]], Field(max_length=20)]],
    'keyword': NotRequired[Annotated[str, Field(max_length=120)]],
    'keywords': NotRequired[Annotated[list[Annotated[str, Field(min_length=1, max_length=120)]], Field(max_length=20)]],
    'relatedEntityId': NotRequired[Annotated[str, Field(max_length=80)]],
    'trailId': NotRequired[Annotated[str, Field(max_length=80)]],
    'sourceDomain': NotRequired[Annotated[str, Field(max_length=240)]],
    'hasMedia': NotRequired[bool],
    'hasVideo': NotRequired[bool],
    'publishedAfter': NotRequired[Annotated[str, Field(max_length=80)]],
    'updatedAfter': NotRequired[Annotated[str, Field(max_length=80)]],
    'filterId': NotRequired[Annotated[str, Field(max_length=200)]],
    'limit': NotRequired[Annotated[int, Field(ge=1, le=100)]],
    'offset': NotRequired[Annotated[int, Field(ge=0, le=10000)]],
})
CommonsSaveFilterInputFilter.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class CommonsSaveFilterInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    name: Annotated[str, Field(min_length=2, max_length=80)] = Field(..., alias='name', description='User-facing name for this MCP personalization filter. Reusing a name updates the saved filter.')
    description: Union[Annotated[str, Field(max_length=500)], None] = Field(None, alias='description', description='Optional note explaining when this filter should be used.')
    filter: CommonsSaveFilterInputFilter = Field(..., alias='filter', description='Search/filter scope to save for this account, such as a category, trail, source domain, tags, or media constraints.')


class CommonsSaveFilterOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    data: Union[Any, None] = Field(None, alias='data', description='')
    error: Union[str, None] = Field(None, alias='error', description='')
    message: Union[str, None] = Field(None, alias='message', description='')


CommonsSaveFilterOutputVariant2DeliveryArtifactsItem = TypedDict('CommonsSaveFilterOutputVariant2DeliveryArtifactsItem', {
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
CommonsSaveFilterOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsSaveFilterOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CommonsSaveFilterOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CommonsSaveFilterOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsSaveFilterOutputVariant2Delivery = TypedDict('CommonsSaveFilterOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CommonsSaveFilterOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CommonsSaveFilterOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CommonsSaveFilterOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsSaveFilterOutputVariant2RecoveryOperation = TypedDict('CommonsSaveFilterOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CommonsSaveFilterOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsSaveFilterOutputVariant2Recovery = TypedDict('CommonsSaveFilterOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CommonsSaveFilterOutputVariant2RecoveryOperation],
})
CommonsSaveFilterOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CommonsSaveFilterOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CommonsSaveFilterOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CommonsSaveFilterOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CommonsSaveFilterOutput).
CommonsSaveFilterOutput = Union[CommonsSaveFilterOutputVariant2, CommonsSaveFilterOutputVariant1]

_CommonsSaveFilterInputAdapter = TypeAdapter(CommonsSaveFilterInput)
_CommonsSaveFilterOutputAdapter = TypeAdapter(CommonsSaveFilterOutput)