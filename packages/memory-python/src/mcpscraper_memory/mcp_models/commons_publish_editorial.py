from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


CommonsPublishEditorialInputSiteOgImage = TypedDict('CommonsPublishEditorialInputSiteOgImage', {
    'url': Required[str],
    'alt': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'width': NotRequired[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'height': NotRequired[Annotated[int, Field(le=9007199254740991, gt=0)]],
})
CommonsPublishEditorialInputSiteOgImage.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CommonsPublishEditorialInputSite = TypedDict('CommonsPublishEditorialInputSite', {
    'slug': Required[Annotated[str, Field(max_length=80)]],
    'title': Required[Annotated[str, Field(min_length=1, max_length=140)]],
    'product': Required[Annotated[str, Field(min_length=1, max_length=80)]],
    'edition': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'editionLabel': NotRequired[Annotated[str, Field(min_length=1, max_length=100)]],
    'issueLabel': NotRequired[Annotated[str, Field(min_length=1, max_length=100)]],
    'eyebrow': NotRequired[Annotated[str, Field(min_length=1, max_length=120)]],
    'heroTitle': Required[Annotated[str, Field(min_length=1, max_length=180)]],
    'startLabel': NotRequired[Annotated[str, Field(min_length=1, max_length=60)]],
    'ogImage': NotRequired[CommonsPublishEditorialInputSiteOgImage],
})
CommonsPublishEditorialInputSite.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CommonsPublishEditorialInputArticlesItemImage = TypedDict('CommonsPublishEditorialInputArticlesItemImage', {
    'url': Required[str],
    'alt': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'caption': NotRequired[Annotated[str, Field(max_length=1000)]],
    'credit': NotRequired[Annotated[str, Field(max_length=500)]],
    'sourceUrl': NotRequired[str],
    'width': NotRequired[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'height': NotRequired[Annotated[int, Field(le=9007199254740991, gt=0)]],
})
CommonsPublishEditorialInputArticlesItemImage.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CommonsPublishEditorialInputArticlesItemOgImage = TypedDict('CommonsPublishEditorialInputArticlesItemOgImage', {
    'url': Required[str],
    'alt': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'caption': NotRequired[Annotated[str, Field(max_length=1000)]],
    'credit': NotRequired[Annotated[str, Field(max_length=500)]],
    'sourceUrl': NotRequired[str],
    'width': NotRequired[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'height': NotRequired[Annotated[int, Field(le=9007199254740991, gt=0)]],
})
CommonsPublishEditorialInputArticlesItemOgImage.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CommonsPublishEditorialInputArticlesItem = TypedDict('CommonsPublishEditorialInputArticlesItem', {
    'slug': Required[Annotated[str, Field(max_length=80)]],
    'category': Required[Annotated[str, Field(min_length=1, max_length=80)]],
    'kicker': Required[Annotated[str, Field(min_length=1, max_length=140)]],
    'order': Required[Annotated[int, Field(ge=1, le=1000)]],
    'title': Required[Annotated[str, Field(min_length=1, max_length=180)]],
    'summary': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'sourceType': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'sourceLabel': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'revision': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'updatedAt': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'image': NotRequired[CommonsPublishEditorialInputArticlesItemImage],
    'ogImage': NotRequired[CommonsPublishEditorialInputArticlesItemOgImage],
    'markdown': Required[Annotated[str, Field(min_length=1, max_length=100000)]],
})
CommonsPublishEditorialInputArticlesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class CommonsPublishEditorialInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    publication_subdomain: Annotated[str, Field(min_length=3, max_length=50)] = Field(..., alias='publicationSubdomain', description='Publication owned by the authenticated account.')
    edition_slug: Union[Annotated[str, Field(max_length=80)], None] = Field(None, alias='editionSlug', description='Stable public edition slug. Defaults to site.slug.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Unique key for this intended publish. Reuse it only when retrying the same revision.')
    base_revision: Union[Annotated[int, Field(le=9007199254740991, gt=0)], None] = Field(None, alias='baseRevision', description='Required when revising an existing edition; use the current revision from commons_get_publication.')
    site: CommonsPublishEditorialInputSite = Field(..., alias='site', description='Complete editorial site payload containing the collection identity and authored articles.')
    deck: Annotated[str, Field(min_length=1, max_length=1000)] = Field(..., alias='deck', description='Two or three sentences that explain the collection’s value and scope without generic marketing language.')
    articles: Annotated[list[CommonsPublishEditorialInputArticlesItem], Field(min_length=1, max_length=100)] = Field(..., alias='articles', description='One to one hundred fully authored articles, with no more than 2,000,000 Markdown bytes combined. Articles may include structured card/hero images, article-specific Open Graph images, and Markdown body images. Read all in-scope source material before composing them; preserve distinctions, uncertainty, image provenance, and rights context instead of flattening the corpus.')
    filename: Union[Annotated[str, Field(max_length=120)], None] = Field(None, alias='filename', description='Optional download filename. The server always normalizes it to a safe .html filename.')


class CommonsPublishEditorialOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    data: Union[Any, None] = Field(None, alias='data', description='')
    error: Union[str, None] = Field(None, alias='error', description='')
    message: Union[str, None] = Field(None, alias='message', description='')


CommonsPublishEditorialOutputVariant2DeliveryArtifactsItem = TypedDict('CommonsPublishEditorialOutputVariant2DeliveryArtifactsItem', {
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
CommonsPublishEditorialOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsPublishEditorialOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CommonsPublishEditorialOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CommonsPublishEditorialOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsPublishEditorialOutputVariant2Delivery = TypedDict('CommonsPublishEditorialOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CommonsPublishEditorialOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CommonsPublishEditorialOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CommonsPublishEditorialOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsPublishEditorialOutputVariant2RecoveryOperation = TypedDict('CommonsPublishEditorialOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CommonsPublishEditorialOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsPublishEditorialOutputVariant2Recovery = TypedDict('CommonsPublishEditorialOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CommonsPublishEditorialOutputVariant2RecoveryOperation],
})
CommonsPublishEditorialOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CommonsPublishEditorialOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CommonsPublishEditorialOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CommonsPublishEditorialOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CommonsPublishEditorialOutput).
CommonsPublishEditorialOutput = Union[CommonsPublishEditorialOutputVariant2, CommonsPublishEditorialOutputVariant1]

_CommonsPublishEditorialInputAdapter = TypeAdapter(CommonsPublishEditorialInput)
_CommonsPublishEditorialOutputAdapter = TypeAdapter(CommonsPublishEditorialOutput)