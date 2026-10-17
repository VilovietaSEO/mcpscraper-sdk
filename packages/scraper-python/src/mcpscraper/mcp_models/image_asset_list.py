from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ImageAssetListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Union[str, None] = Field(None, alias='vault', description='Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.')
    project_id: Union[str, None] = Field(None, alias='projectId', description='Opaque image project identifier returned by an image project tool.')
    folder_id: Union[str, None] = Field(None, alias='folderId', description='Opaque image folder identifier; omit only when the project root is intended.')
    source_kind: Union[Literal['upload', 'scrape', 'screenshot', 'instagram', 'external_url', 'import'], None] = Field(None, alias='sourceKind', description='Provenance category used to filter or label governed image assets.')
    source_host: Union[Annotated[str, Field(min_length=1, max_length=253)], None] = Field(None, alias='sourceHost', description='Normalized source hostname filter without a URL path.')
    mime_type: Union[Literal['image/jpeg', 'image/png', 'image/webp', 'image/gif'], None] = Field(None, alias='mimeType', description='Exact media-type filter, such as image/png; omit for every supported image type.')
    tags: Union[Annotated[list[Annotated[str, Field(min_length=1, max_length=80)]], Field(max_length=20)], None] = Field(None, alias='tags', description='Canonical tag filter or tag set; use the appropriate vocabulary-listing tool before writing new tags.')
    created_after: Union[str, None] = Field(None, alias='createdAfter', description='Inclusive ISO 8601 lower bound for asset creation time.')
    created_before: Union[str, None] = Field(None, alias='createdBefore', description='Exclusive ISO 8601 upper bound for asset creation time.')
    limit: Union[Annotated[int, Field(ge=1, le=100)], None] = Field(None, alias='limit', description='Maximum rows or records to return on this page; use the returned cursor for more.')


ImageAssetListOutputVariant1AssetsItemPreview = TypedDict('ImageAssetListOutputVariant1AssetsItemPreview', {
    'url': Required[str],
    'expiresAt': Required[str],
    'mimeType': Required[Literal['image/webp']],
})
ImageAssetListOutputVariant1AssetsItemPreview.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetListOutputVariant1AssetsItem = TypedDict('ImageAssetListOutputVariant1AssetsItem', {
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
    'preview': NotRequired[ImageAssetListOutputVariant1AssetsItemPreview],
})
ImageAssetListOutputVariant1AssetsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ImageAssetListOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    assets: Union[list[ImageAssetListOutputVariant1AssetsItem], None] = Field(None, alias='assets', description='')
    count: Union[Union[float, int], None] = Field(None, alias='count', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


ImageAssetListOutputVariant2DeliveryArtifactsItem = TypedDict('ImageAssetListOutputVariant2DeliveryArtifactsItem', {
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
ImageAssetListOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetListOutputVariant2DeliveryAvailableExportsItem = TypedDict('ImageAssetListOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
ImageAssetListOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetListOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ImageAssetListOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ImageAssetListOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetListOutputVariant2Delivery = TypedDict('ImageAssetListOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ImageAssetListOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[ImageAssetListOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ImageAssetListOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ImageAssetListOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetListOutputVariant2RecoveryOperation = TypedDict('ImageAssetListOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ImageAssetListOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetListOutputVariant2Recovery = TypedDict('ImageAssetListOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ImageAssetListOutputVariant2RecoveryOperation],
})
ImageAssetListOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ImageAssetListOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ImageAssetListOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ImageAssetListOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ImageAssetListOutput).
ImageAssetListOutput = Union[ImageAssetListOutputVariant2, ImageAssetListOutputVariant1]

_ImageAssetListInputAdapter = TypeAdapter(ImageAssetListInput)
_ImageAssetListOutputAdapter = TypeAdapter(ImageAssetListOutput)