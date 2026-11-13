from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ImageAssetSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Union[str, None] = Field(None, alias='vault', description='Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.')
    query_text: Union[Annotated[str, Field(min_length=1, max_length=4000)], None] = Field(None, alias='queryText', description='Semantic text query for image retrieval; it may be combined with one image-query source.')
    query_asset_id: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='queryAssetId', description='Stored image asset to use as the visual search query; use only one image-query source.')
    query_url: Union[str, None] = Field(None, alias='queryUrl', description='Public HTTPS image URL to use as the visual search query; use only one image-query source.')
    query_image_base64: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='queryImageBase64', description='Bounded base64 image bytes to use as the visual search query; use only one image-query source.')
    project_id: Union[str, None] = Field(None, alias='projectId', description='Opaque image project identifier returned by an image project tool.')
    folder_id: Union[str, None] = Field(None, alias='folderId', description='Opaque image folder identifier; omit only when the project root is intended.')
    source_kind: Union[Literal['upload', 'scrape', 'screenshot', 'instagram', 'external_url', 'import'], None] = Field(None, alias='sourceKind', description='Provenance category used to filter or label governed image assets.')
    source_host: Union[Annotated[str, Field(min_length=1, max_length=253)], None] = Field(None, alias='sourceHost', description='Normalized source hostname filter without a URL path.')
    mime_type: Union[Literal['image/jpeg', 'image/png', 'image/webp', 'image/gif'], None] = Field(None, alias='mimeType', description='Exact media-type filter, such as image/png; omit for every supported image type.')
    tags: Union[Annotated[list[Annotated[str, Field(min_length=1, max_length=80)]], Field(max_length=20)], None] = Field(None, alias='tags', description='Canonical tag filter or tag set; use the appropriate vocabulary-listing tool before writing new tags.')
    created_after: Union[str, None] = Field(None, alias='createdAfter', description='Inclusive ISO 8601 lower bound for asset creation time.')
    created_before: Union[str, None] = Field(None, alias='createdBefore', description='Exclusive ISO 8601 upper bound for asset creation time.')
    limit: Union[Annotated[int, Field(ge=1, le=30)], None] = Field(None, alias='limit', description='Maximum rows or records to return on this page; use the returned cursor for more.')
    include_preview: Union[bool, None] = Field(None, alias='includePreview', description='When true, mint a short-lived authorized preview URL with the metadata result.')


ImageAssetSearchOutputVariant1ResultsItemAssetPreview = TypedDict('ImageAssetSearchOutputVariant1ResultsItemAssetPreview', {
    'url': Required[str],
    'expiresAt': Required[str],
    'mimeType': Required[Literal['image/webp']],
})
ImageAssetSearchOutputVariant1ResultsItemAssetPreview.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetSearchOutputVariant1ResultsItemAsset = TypedDict('ImageAssetSearchOutputVariant1ResultsItemAsset', {
    'assetId': Required[str],
    'title': Required[str],
    'description': Required[Union[str, None]],
    'altText': Required[Union[str, None]],
    'sourceUrl': Required[Union[str, None]],
    'sourceKind': Required[str],
    'mimeType': Required[str],
    'bytes': Required[Union[float, int]],
    'sha256': Required[str],
    'width': Required[Union[float, int]],
    'height': Required[Union[float, int]],
    'projectId': Required[Union[str, None]],
    'folderId': Required[Union[str, None]],
    'tags': Required[list[str]],
    'status': Required[str],
    'embeddingStatus': Required[str],
    'createdAt': Required[str],
    'updatedAt': Required[str],
    'preview': NotRequired[ImageAssetSearchOutputVariant1ResultsItemAssetPreview],
})
ImageAssetSearchOutputVariant1ResultsItemAsset.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetSearchOutputVariant1ResultsItem = TypedDict('ImageAssetSearchOutputVariant1ResultsItem', {
    'asset': Required[ImageAssetSearchOutputVariant1ResultsItemAsset],
    'score': Required[Union[float, int]],
    'matchRepresentations': Required[list[Literal['visual', 'fused']]],
    'embeddingModel': Required[str],
})
ImageAssetSearchOutputVariant1ResultsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ImageAssetSearchOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    results: Union[list[ImageAssetSearchOutputVariant1ResultsItem], None] = Field(None, alias='results', description='')
    count: Union[Union[float, int], None] = Field(None, alias='count', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


ImageAssetSearchOutputVariant2DeliveryArtifactsItem = TypedDict('ImageAssetSearchOutputVariant2DeliveryArtifactsItem', {
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
ImageAssetSearchOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetSearchOutputVariant2DeliveryAvailableExportsItem = TypedDict('ImageAssetSearchOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
ImageAssetSearchOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetSearchOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ImageAssetSearchOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ImageAssetSearchOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetSearchOutputVariant2Delivery = TypedDict('ImageAssetSearchOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ImageAssetSearchOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[ImageAssetSearchOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ImageAssetSearchOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ImageAssetSearchOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetSearchOutputVariant2RecoveryOperation = TypedDict('ImageAssetSearchOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ImageAssetSearchOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetSearchOutputVariant2Recovery = TypedDict('ImageAssetSearchOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ImageAssetSearchOutputVariant2RecoveryOperation],
})
ImageAssetSearchOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ImageAssetSearchOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ImageAssetSearchOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ImageAssetSearchOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ImageAssetSearchOutput).
ImageAssetSearchOutput = Union[ImageAssetSearchOutputVariant2, ImageAssetSearchOutputVariant1]

_ImageAssetSearchInputAdapter = TypeAdapter(ImageAssetSearchInput)
_ImageAssetSearchOutputAdapter = TypeAdapter(ImageAssetSearchOutput)