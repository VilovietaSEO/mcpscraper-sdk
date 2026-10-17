from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CommonsUpdateEditorialArticleInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    publication_subdomain: Annotated[str, Field(min_length=3, max_length=50)] = Field(..., alias='publicationSubdomain', description='Publication owned by the authenticated account.')
    edition_slug: Union[Annotated[str, Field(max_length=80)], None] = Field(None, alias='editionSlug', description='Edition holding the article. Defaults to the publication’s latest edition.')
    article_slug: Annotated[str, Field(max_length=80)] = Field(..., alias='articleSlug', description='Slug of the one article to replace, from commons_get_publication with includeArticles.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Unique key for this intended edit. Reuse it only when retrying the same edit.')
    base_revision: Annotated[int, Field(le=9007199254740991, gt=0)] = Field(..., alias='baseRevision', description='Current edition revision from commons_get_publication. The edit is refused if the edition moved on.')
    markdown: Union[Annotated[str, Field(min_length=1, max_length=400000)], None] = Field(None, alias='markdown', description='Replacement Markdown body for this article. Omit to change only the metadata fields below.')
    title: Union[Annotated[str, Field(min_length=1, max_length=180)], None] = Field(None, alias='title', description='Replacement article title.')
    summary: Union[Annotated[str, Field(min_length=1, max_length=500)], None] = Field(None, alias='summary', description='Replacement one or two sentence summary.')
    category: Union[Annotated[str, Field(min_length=1, max_length=80)], None] = Field(None, alias='category', description='Replacement section label.')
    kicker: Union[Annotated[str, Field(min_length=1, max_length=140)], None] = Field(None, alias='kicker', description='Replacement framing line above the title.')
    order: Union[Annotated[int, Field(ge=1, le=1000)], None] = Field(None, alias='order', description='Replacement reading-order position.')


class CommonsUpdateEditorialArticleOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    data: Union[Any, None] = Field(None, alias='data', description='')
    error: Union[str, None] = Field(None, alias='error', description='')
    message: Union[str, None] = Field(None, alias='message', description='')


CommonsUpdateEditorialArticleOutputVariant2DeliveryArtifactsItem = TypedDict('CommonsUpdateEditorialArticleOutputVariant2DeliveryArtifactsItem', {
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
CommonsUpdateEditorialArticleOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsUpdateEditorialArticleOutputVariant2DeliveryAvailableExportsItem = TypedDict('CommonsUpdateEditorialArticleOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CommonsUpdateEditorialArticleOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsUpdateEditorialArticleOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CommonsUpdateEditorialArticleOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CommonsUpdateEditorialArticleOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsUpdateEditorialArticleOutputVariant2Delivery = TypedDict('CommonsUpdateEditorialArticleOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CommonsUpdateEditorialArticleOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CommonsUpdateEditorialArticleOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CommonsUpdateEditorialArticleOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CommonsUpdateEditorialArticleOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsUpdateEditorialArticleOutputVariant2RecoveryOperation = TypedDict('CommonsUpdateEditorialArticleOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CommonsUpdateEditorialArticleOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsUpdateEditorialArticleOutputVariant2Recovery = TypedDict('CommonsUpdateEditorialArticleOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CommonsUpdateEditorialArticleOutputVariant2RecoveryOperation],
})
CommonsUpdateEditorialArticleOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CommonsUpdateEditorialArticleOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CommonsUpdateEditorialArticleOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CommonsUpdateEditorialArticleOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CommonsUpdateEditorialArticleOutput).
CommonsUpdateEditorialArticleOutput = Union[CommonsUpdateEditorialArticleOutputVariant2, CommonsUpdateEditorialArticleOutputVariant1]

_CommonsUpdateEditorialArticleInputAdapter = TypeAdapter(CommonsUpdateEditorialArticleInput)
_CommonsUpdateEditorialArticleOutputAdapter = TypeAdapter(CommonsUpdateEditorialArticleOutput)