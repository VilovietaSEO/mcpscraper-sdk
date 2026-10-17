from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


CommonsValidatePublicationInputEditionSiteOgImage = TypedDict('CommonsValidatePublicationInputEditionSiteOgImage', {
    'url': Required[str],
    'alt': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'width': NotRequired[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'height': NotRequired[Annotated[int, Field(le=9007199254740991, gt=0)]],
})
CommonsValidatePublicationInputEditionSiteOgImage.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CommonsValidatePublicationInputEditionSite = TypedDict('CommonsValidatePublicationInputEditionSite', {
    'slug': Required[Annotated[str, Field(max_length=80)]],
    'title': Required[Annotated[str, Field(min_length=1, max_length=140)]],
    'product': Required[Annotated[str, Field(min_length=1, max_length=80)]],
    'edition': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'editionLabel': NotRequired[Annotated[str, Field(min_length=1, max_length=100)]],
    'issueLabel': NotRequired[Annotated[str, Field(min_length=1, max_length=100)]],
    'eyebrow': NotRequired[Annotated[str, Field(min_length=1, max_length=120)]],
    'heroTitle': Required[Annotated[str, Field(min_length=1, max_length=180)]],
    'startLabel': NotRequired[Annotated[str, Field(min_length=1, max_length=60)]],
    'ogImage': NotRequired[CommonsValidatePublicationInputEditionSiteOgImage],
})
CommonsValidatePublicationInputEditionSite.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CommonsValidatePublicationInputEditionArticlesItemImage = TypedDict('CommonsValidatePublicationInputEditionArticlesItemImage', {
    'url': Required[str],
    'alt': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'caption': NotRequired[Annotated[str, Field(max_length=1000)]],
    'credit': NotRequired[Annotated[str, Field(max_length=500)]],
    'sourceUrl': NotRequired[str],
    'width': NotRequired[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'height': NotRequired[Annotated[int, Field(le=9007199254740991, gt=0)]],
})
CommonsValidatePublicationInputEditionArticlesItemImage.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CommonsValidatePublicationInputEditionArticlesItemOgImage = TypedDict('CommonsValidatePublicationInputEditionArticlesItemOgImage', {
    'url': Required[str],
    'alt': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'caption': NotRequired[Annotated[str, Field(max_length=1000)]],
    'credit': NotRequired[Annotated[str, Field(max_length=500)]],
    'sourceUrl': NotRequired[str],
    'width': NotRequired[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'height': NotRequired[Annotated[int, Field(le=9007199254740991, gt=0)]],
})
CommonsValidatePublicationInputEditionArticlesItemOgImage.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CommonsValidatePublicationInputEditionArticlesItem = TypedDict('CommonsValidatePublicationInputEditionArticlesItem', {
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
    'image': NotRequired[CommonsValidatePublicationInputEditionArticlesItemImage],
    'ogImage': NotRequired[CommonsValidatePublicationInputEditionArticlesItemOgImage],
    'markdown': Required[Annotated[str, Field(min_length=1, max_length=100000)]],
})
CommonsValidatePublicationInputEditionArticlesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CommonsValidatePublicationInputEdition = TypedDict('CommonsValidatePublicationInputEdition', {
    'site': Required[CommonsValidatePublicationInputEditionSite],
    'deck': Required[Annotated[str, Field(min_length=1, max_length=1000)]],
    'articles': Required[Annotated[list[CommonsValidatePublicationInputEditionArticlesItem], Field(min_length=1, max_length=100)]],
    'filename': NotRequired[Annotated[str, Field(max_length=120)]],
})
CommonsValidatePublicationInputEdition.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class CommonsValidatePublicationInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    operation: Literal['claim', 'publish'] = Field(..., alias='operation', description='Validate either a new name claim or a finished editorial edition without writing.')
    requested_subdomain: Union[Annotated[str, Field(min_length=3, max_length=50)], None] = Field(None, alias='requestedSubdomain', description='Publication name to validate when operation is claim.')
    publication_subdomain: Union[Annotated[str, Field(min_length=3, max_length=50)], None] = Field(None, alias='publicationSubdomain', description='Already claimed publication name to validate when operation is publish.')
    title: Union[Annotated[str, Field(min_length=1, max_length=140)], None] = Field(None, alias='title', description='Human-readable title for the proposed record or authored content.')
    description: Union[Annotated[str, Field(max_length=500)], None] = Field(None, alias='description', description='Human-readable summary that distinguishes this record from similarly named records.')
    edition: Union[CommonsValidatePublicationInputEdition, None] = Field(None, alias='edition', description='Complete source-grounded reading-room payload to validate when operation is publish.')
    edition_slug: Union[Annotated[str, Field(max_length=80)], None] = Field(None, alias='editionSlug', description='Stable public edition slug. Defaults to edition.site.slug.')
    base_revision: Union[Annotated[int, Field(le=9007199254740991, gt=0)], None] = Field(None, alias='baseRevision', description='Current edition revision when validating an edit.')


class CommonsValidatePublicationOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    data: Union[Any, None] = Field(None, alias='data', description='')
    error: Union[str, None] = Field(None, alias='error', description='')
    message: Union[str, None] = Field(None, alias='message', description='')


CommonsValidatePublicationOutputVariant2DeliveryArtifactsItem = TypedDict('CommonsValidatePublicationOutputVariant2DeliveryArtifactsItem', {
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
CommonsValidatePublicationOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsValidatePublicationOutputVariant2DeliveryAvailableExportsItem = TypedDict('CommonsValidatePublicationOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CommonsValidatePublicationOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsValidatePublicationOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CommonsValidatePublicationOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CommonsValidatePublicationOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsValidatePublicationOutputVariant2Delivery = TypedDict('CommonsValidatePublicationOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CommonsValidatePublicationOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CommonsValidatePublicationOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CommonsValidatePublicationOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CommonsValidatePublicationOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsValidatePublicationOutputVariant2RecoveryOperation = TypedDict('CommonsValidatePublicationOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CommonsValidatePublicationOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsValidatePublicationOutputVariant2Recovery = TypedDict('CommonsValidatePublicationOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CommonsValidatePublicationOutputVariant2RecoveryOperation],
})
CommonsValidatePublicationOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CommonsValidatePublicationOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CommonsValidatePublicationOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CommonsValidatePublicationOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CommonsValidatePublicationOutput).
CommonsValidatePublicationOutput = Union[CommonsValidatePublicationOutputVariant2, CommonsValidatePublicationOutputVariant1]

_CommonsValidatePublicationInputAdapter = TypeAdapter(CommonsValidatePublicationInput)
_CommonsValidatePublicationOutputAdapter = TypeAdapter(CommonsValidatePublicationOutput)