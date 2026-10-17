from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


CreateEditorialReadingRoomInputSiteOgImage = TypedDict('CreateEditorialReadingRoomInputSiteOgImage', {
    'url': Required[str],
    'alt': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'width': NotRequired[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'height': NotRequired[Annotated[int, Field(le=9007199254740991, gt=0)]],
})
CreateEditorialReadingRoomInputSiteOgImage.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateEditorialReadingRoomInputSite = TypedDict('CreateEditorialReadingRoomInputSite', {
    'slug': Required[Annotated[str, Field(max_length=80)]],
    'title': Required[Annotated[str, Field(min_length=1, max_length=140)]],
    'product': Required[Annotated[str, Field(min_length=1, max_length=80)]],
    'edition': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'editionLabel': NotRequired[Annotated[str, Field(min_length=1, max_length=100)]],
    'issueLabel': NotRequired[Annotated[str, Field(min_length=1, max_length=100)]],
    'eyebrow': NotRequired[Annotated[str, Field(min_length=1, max_length=120)]],
    'heroTitle': Required[Annotated[str, Field(min_length=1, max_length=180)]],
    'startLabel': NotRequired[Annotated[str, Field(min_length=1, max_length=60)]],
    'ogImage': NotRequired[CreateEditorialReadingRoomInputSiteOgImage],
})
CreateEditorialReadingRoomInputSite.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateEditorialReadingRoomInputArticlesItemImage = TypedDict('CreateEditorialReadingRoomInputArticlesItemImage', {
    'url': Required[str],
    'alt': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'caption': NotRequired[Annotated[str, Field(max_length=1000)]],
    'credit': NotRequired[Annotated[str, Field(max_length=500)]],
    'sourceUrl': NotRequired[str],
    'width': NotRequired[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'height': NotRequired[Annotated[int, Field(le=9007199254740991, gt=0)]],
})
CreateEditorialReadingRoomInputArticlesItemImage.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateEditorialReadingRoomInputArticlesItemOgImage = TypedDict('CreateEditorialReadingRoomInputArticlesItemOgImage', {
    'url': Required[str],
    'alt': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'caption': NotRequired[Annotated[str, Field(max_length=1000)]],
    'credit': NotRequired[Annotated[str, Field(max_length=500)]],
    'sourceUrl': NotRequired[str],
    'width': NotRequired[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'height': NotRequired[Annotated[int, Field(le=9007199254740991, gt=0)]],
})
CreateEditorialReadingRoomInputArticlesItemOgImage.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateEditorialReadingRoomInputArticlesItem = TypedDict('CreateEditorialReadingRoomInputArticlesItem', {
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
    'image': NotRequired[CreateEditorialReadingRoomInputArticlesItemImage],
    'ogImage': NotRequired[CreateEditorialReadingRoomInputArticlesItemOgImage],
    'markdown': Required[Annotated[str, Field(min_length=1, max_length=100000)]],
})
CreateEditorialReadingRoomInputArticlesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class CreateEditorialReadingRoomInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site: CreateEditorialReadingRoomInputSite = Field(..., alias='site', description='Complete editorial site payload containing the collection identity and authored articles.')
    deck: Annotated[str, Field(min_length=1, max_length=1000)] = Field(..., alias='deck', description='Two or three sentences that explain the collection’s value and scope without generic marketing language.')
    articles: Annotated[list[CreateEditorialReadingRoomInputArticlesItem], Field(min_length=1, max_length=100)] = Field(..., alias='articles', description='One to one hundred fully authored articles, with no more than 2,000,000 Markdown bytes combined. Articles may include structured card/hero images, article-specific Open Graph images, and Markdown body images. Read all in-scope source material before composing them; preserve distinctions, uncertainty, image provenance, and rights context instead of flattening the corpus.')
    filename: Union[Annotated[str, Field(max_length=120)], None] = Field(None, alias='filename', description='Optional download filename. The server always normalizes it to a safe .html filename.')


CreateEditorialReadingRoomOutputVariant1Artifact = TypedDict('CreateEditorialReadingRoomOutputVariant1Artifact', {
    'artifactId': Required[str],
    'filename': Required[str],
    'contentType': Required[Literal['text/html']],
    'bytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'sha256': Required[str],
    'expiresAt': Required[str],
    'downloadUrl': Required[Union[str, None]],
    'downloadUrlExpiresAt': Required[Union[str, None]],
})
CreateEditorialReadingRoomOutputVariant1Artifact.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CreateEditorialReadingRoomOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    title: str = Field(..., alias='title', description='')
    filename: str = Field(..., alias='filename', description='')
    delivery: Literal['artifact', 'local_file'] = Field(..., alias='delivery', description='')
    article_count: Annotated[int, Field(ge=1, le=9007199254740991)] = Field(..., alias='articleCount', description='')
    word_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='wordCount', description='')
    bytes: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='bytes', description='')
    sha256: str = Field(..., alias='sha256', description='')
    generated_at: str = Field(..., alias='generatedAt', description='')
    artifact: Union[CreateEditorialReadingRoomOutputVariant1Artifact, None] = Field(None, alias='artifact', description='')
    local_path: Union[str, None] = Field(None, alias='localPath', description='')
    warnings: list[str] = Field(..., alias='warnings', description='')


CreateEditorialReadingRoomOutputVariant2DeliveryArtifactsItem = TypedDict('CreateEditorialReadingRoomOutputVariant2DeliveryArtifactsItem', {
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
CreateEditorialReadingRoomOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateEditorialReadingRoomOutputVariant2DeliveryAvailableExportsItem = TypedDict('CreateEditorialReadingRoomOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CreateEditorialReadingRoomOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateEditorialReadingRoomOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CreateEditorialReadingRoomOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CreateEditorialReadingRoomOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateEditorialReadingRoomOutputVariant2Delivery = TypedDict('CreateEditorialReadingRoomOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CreateEditorialReadingRoomOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CreateEditorialReadingRoomOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CreateEditorialReadingRoomOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CreateEditorialReadingRoomOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateEditorialReadingRoomOutputVariant2RecoveryOperation = TypedDict('CreateEditorialReadingRoomOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CreateEditorialReadingRoomOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateEditorialReadingRoomOutputVariant2Recovery = TypedDict('CreateEditorialReadingRoomOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CreateEditorialReadingRoomOutputVariant2RecoveryOperation],
})
CreateEditorialReadingRoomOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CreateEditorialReadingRoomOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CreateEditorialReadingRoomOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CreateEditorialReadingRoomOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CreateEditorialReadingRoomOutput).
CreateEditorialReadingRoomOutput = Union[CreateEditorialReadingRoomOutputVariant1, CreateEditorialReadingRoomOutputVariant2]

_CreateEditorialReadingRoomInputAdapter = TypeAdapter(CreateEditorialReadingRoomInput)
_CreateEditorialReadingRoomOutputAdapter = TypeAdapter(CreateEditorialReadingRoomOutput)