from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CommonsDeleteEditorialArticleInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    publication_subdomain: Annotated[str, Field(min_length=3, max_length=50)] = Field(..., alias='publicationSubdomain', description='Caller-owned publication containing the article.')
    edition_slug: Union[Annotated[str, Field(max_length=80)], None] = Field(None, alias='editionSlug', description='Edition holding the article. Defaults to the publication’s latest edition.')
    article_slug: Annotated[str, Field(max_length=80)] = Field(..., alias='articleSlug', description='Slug of the article to delete; other articles are preserved.')
    base_revision: Annotated[int, Field(le=9007199254740991, gt=0)] = Field(..., alias='baseRevision', description='Current edition revision from commons_get_publication; stale deletes are rejected.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Unique key for this deletion; reuse only for an exact retry.')


class CommonsDeleteEditorialArticleOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    data: Union[Any, None] = Field(None, alias='data', description='')
    error: Union[str, None] = Field(None, alias='error', description='')
    message: Union[str, None] = Field(None, alias='message', description='')


CommonsDeleteEditorialArticleOutputVariant2DeliveryArtifactsItem = TypedDict('CommonsDeleteEditorialArticleOutputVariant2DeliveryArtifactsItem', {
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
CommonsDeleteEditorialArticleOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsDeleteEditorialArticleOutputVariant2DeliveryAvailableExportsItem = TypedDict('CommonsDeleteEditorialArticleOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CommonsDeleteEditorialArticleOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsDeleteEditorialArticleOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CommonsDeleteEditorialArticleOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CommonsDeleteEditorialArticleOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsDeleteEditorialArticleOutputVariant2Delivery = TypedDict('CommonsDeleteEditorialArticleOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CommonsDeleteEditorialArticleOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CommonsDeleteEditorialArticleOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CommonsDeleteEditorialArticleOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CommonsDeleteEditorialArticleOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsDeleteEditorialArticleOutputVariant2RecoveryOperation = TypedDict('CommonsDeleteEditorialArticleOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CommonsDeleteEditorialArticleOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsDeleteEditorialArticleOutputVariant2Recovery = TypedDict('CommonsDeleteEditorialArticleOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CommonsDeleteEditorialArticleOutputVariant2RecoveryOperation],
})
CommonsDeleteEditorialArticleOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CommonsDeleteEditorialArticleOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CommonsDeleteEditorialArticleOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CommonsDeleteEditorialArticleOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CommonsDeleteEditorialArticleOutput).
CommonsDeleteEditorialArticleOutput = Union[CommonsDeleteEditorialArticleOutputVariant2, CommonsDeleteEditorialArticleOutputVariant1]

_CommonsDeleteEditorialArticleInputAdapter = TypeAdapter(CommonsDeleteEditorialArticleInput)
_CommonsDeleteEditorialArticleOutputAdapter = TypeAdapter(CommonsDeleteEditorialArticleOutput)