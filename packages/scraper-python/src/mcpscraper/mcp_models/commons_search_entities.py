from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CommonsSearchEntitiesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    mode: Union[Literal['lexical', 'semantic', 'hybrid'], None] = Field(None, alias='mode', description='Retrieval mode. hybrid (default) fuses meaning-based candidates with exact term matching; lexical matches terms only, which is what you want when the caller quoted an exact name or phrase; semantic ignores term matching entirely.')
    query: Union[Annotated[str, Field(max_length=300)], None] = Field(None, alias='query', description='Search text matched against title, description, tags, keywords, JSON-LD, source metadata, citations, media, and article body.')
    entity_type: Union[Annotated[str, Field(max_length=120)], None] = Field(None, alias='entityType', description='Optional entity type filter. "Public Article", "PublicArticle", "Article", and "item" normalize to PublicArticle.')
    tag: Union[Annotated[str, Field(max_length=80)], None] = Field(None, alias='tag', description='Single canonical tag filter. Use tags for multiple tags.')
    tags: Union[Annotated[list[Annotated[str, Field(min_length=1, max_length=80)]], Field(max_length=20)], None] = Field(None, alias='tags', description='Multiple tag filters. All supplied tags are applied.')
    keyword: Union[Annotated[str, Field(max_length=120)], None] = Field(None, alias='keyword', description='Single keyword filter. Use keywords for multiple keywords.')
    keywords: Union[Annotated[list[Annotated[str, Field(min_length=1, max_length=120)]], Field(max_length=20)], None] = Field(None, alias='keywords', description='Multiple keyword filters. All supplied keywords are applied.')
    related_entity_id: Union[Annotated[str, Field(max_length=80)], None] = Field(None, alias='relatedEntityId', description='Return entities related to this Transparent Public Wiki entity id.')
    trail_id: Union[Annotated[str, Field(max_length=80)], None] = Field(None, alias='trailId', description='Return entities collected into a specific reading trail entity.')
    source_domain: Union[Annotated[str, Field(max_length=240)], None] = Field(None, alias='sourceDomain', description='Filter by original-source or canonical-source domain text.')
    has_media: Union[bool, None] = Field(None, alias='hasMedia', description='When true, only return entities with image, video, or audio media records.')
    has_video: Union[bool, None] = Field(None, alias='hasVideo', description='When true, only return entities with at least one video media record.')
    published_after: Union[Annotated[str, Field(max_length=80)], None] = Field(None, alias='publishedAfter', description='Optional ISO-ish lower bound for publishedAt.')
    updated_after: Union[Annotated[str, Field(max_length=80)], None] = Field(None, alias='updatedAfter', description='Optional ISO-ish lower bound for updatedAt.')
    filter_id: Union[Annotated[str, Field(max_length=200)], None] = Field(None, alias='filterId', description='Optional saved filter id from commons_list_filters. The saved filter is merged with this call for this account.')
    limit: Union[Annotated[int, Field(ge=1, le=100)], None] = Field(None, alias='limit', description='Maximum entities to return. Default 20, maximum 100.')
    offset: Union[Annotated[int, Field(ge=0, le=10000)], None] = Field(None, alias='offset', description='Pagination offset.')


class CommonsSearchEntitiesOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    data: Union[Any, None] = Field(None, alias='data', description='')
    error: Union[str, None] = Field(None, alias='error', description='')
    message: Union[str, None] = Field(None, alias='message', description='')


CommonsSearchEntitiesOutputVariant2DeliveryArtifactsItem = TypedDict('CommonsSearchEntitiesOutputVariant2DeliveryArtifactsItem', {
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
CommonsSearchEntitiesOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsSearchEntitiesOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CommonsSearchEntitiesOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CommonsSearchEntitiesOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsSearchEntitiesOutputVariant2Delivery = TypedDict('CommonsSearchEntitiesOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CommonsSearchEntitiesOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CommonsSearchEntitiesOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CommonsSearchEntitiesOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsSearchEntitiesOutputVariant2RecoveryOperation = TypedDict('CommonsSearchEntitiesOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CommonsSearchEntitiesOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsSearchEntitiesOutputVariant2Recovery = TypedDict('CommonsSearchEntitiesOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CommonsSearchEntitiesOutputVariant2RecoveryOperation],
})
CommonsSearchEntitiesOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CommonsSearchEntitiesOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CommonsSearchEntitiesOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CommonsSearchEntitiesOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CommonsSearchEntitiesOutput).
CommonsSearchEntitiesOutput = Union[CommonsSearchEntitiesOutputVariant2, CommonsSearchEntitiesOutputVariant1]

_CommonsSearchEntitiesInputAdapter = TypeAdapter(CommonsSearchEntitiesInput)
_CommonsSearchEntitiesOutputAdapter = TypeAdapter(CommonsSearchEntitiesOutput)