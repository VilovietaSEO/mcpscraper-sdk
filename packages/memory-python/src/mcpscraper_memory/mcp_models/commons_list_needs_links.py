from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CommonsListNeedsLinksInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    query: Union[Annotated[str, Field(max_length=300)], None] = Field(None, alias='query', description='Optional text filter over unresolved concept title, summary, relationship, source page title, source description, and source tags.')
    entity_type: Union[Annotated[str, Field(max_length=120)], None] = Field(None, alias='entityType', description='Only return unresolved concepts found on source entities of this type.')
    tag: Union[Annotated[str, Field(max_length=80)], None] = Field(None, alias='tag', description='Only return unresolved concepts found on source entities with this tag.')
    tags: Union[Annotated[list[Annotated[str, Field(min_length=1, max_length=80)]], Field(max_length=20)], None] = Field(None, alias='tags', description='Only return unresolved concepts found on source entities matching all supplied tags.')
    source_entity_id: Union[Annotated[str, Field(max_length=80)], None] = Field(None, alias='sourceEntityId', description='Only return unresolved concepts from one source entity id.')
    source_slug: Union[Annotated[str, Field(max_length=180)], None] = Field(None, alias='sourceSlug', description='Only return unresolved concepts from one /wiki/ source slug.')
    limit: Union[Annotated[int, Field(ge=1, le=100)], None] = Field(None, alias='limit', description='Maximum rows or records to return on this page; use the returned cursor for more.')
    offset: Union[Annotated[int, Field(ge=0, le=10000)], None] = Field(None, alias='offset', description='Zero-based result offset; increase only when continuing the same bounded query.')


class CommonsListNeedsLinksOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    data: Union[Any, None] = Field(None, alias='data', description='')
    error: Union[str, None] = Field(None, alias='error', description='')
    message: Union[str, None] = Field(None, alias='message', description='')


CommonsListNeedsLinksOutputVariant2DeliveryArtifactsItem = TypedDict('CommonsListNeedsLinksOutputVariant2DeliveryArtifactsItem', {
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
CommonsListNeedsLinksOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsListNeedsLinksOutputVariant2DeliveryAvailableExportsItem = TypedDict('CommonsListNeedsLinksOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CommonsListNeedsLinksOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsListNeedsLinksOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CommonsListNeedsLinksOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CommonsListNeedsLinksOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsListNeedsLinksOutputVariant2Delivery = TypedDict('CommonsListNeedsLinksOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CommonsListNeedsLinksOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CommonsListNeedsLinksOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CommonsListNeedsLinksOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CommonsListNeedsLinksOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsListNeedsLinksOutputVariant2RecoveryOperation = TypedDict('CommonsListNeedsLinksOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CommonsListNeedsLinksOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsListNeedsLinksOutputVariant2Recovery = TypedDict('CommonsListNeedsLinksOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CommonsListNeedsLinksOutputVariant2RecoveryOperation],
})
CommonsListNeedsLinksOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CommonsListNeedsLinksOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CommonsListNeedsLinksOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CommonsListNeedsLinksOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CommonsListNeedsLinksOutput).
CommonsListNeedsLinksOutput = Union[CommonsListNeedsLinksOutputVariant2, CommonsListNeedsLinksOutputVariant1]

_CommonsListNeedsLinksInputAdapter = TypeAdapter(CommonsListNeedsLinksInput)
_CommonsListNeedsLinksOutputAdapter = TypeAdapter(CommonsListNeedsLinksOutput)