from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ImageAssetGetInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Union[str, None] = Field(None, alias='vault', description='Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.')
    asset_id: Annotated[str, Field(min_length=1)] = Field(..., alias='assetId', description='Opaque image asset identifier returned by an image asset tool.')
    include_preview: Union[bool, None] = Field(None, alias='includePreview', description='When true, mint a short-lived authorized preview URL with the metadata result.')


ImageAssetGetOutputVariant1AssetPreview = TypedDict('ImageAssetGetOutputVariant1AssetPreview', {
    'url': Required[str],
    'expiresAt': Required[str],
    'mimeType': Required[Literal['image/webp']],
})
ImageAssetGetOutputVariant1AssetPreview.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetGetOutputVariant1Asset = TypedDict('ImageAssetGetOutputVariant1Asset', {
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
    'preview': NotRequired[ImageAssetGetOutputVariant1AssetPreview],
})
ImageAssetGetOutputVariant1Asset.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ImageAssetGetOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    asset: Union[ImageAssetGetOutputVariant1Asset, None] = Field(None, alias='asset', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


ImageAssetGetOutputVariant2DeliveryArtifactsItem = TypedDict('ImageAssetGetOutputVariant2DeliveryArtifactsItem', {
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
ImageAssetGetOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetGetOutputVariant2DeliveryAvailableExportsItem = TypedDict('ImageAssetGetOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
ImageAssetGetOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetGetOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ImageAssetGetOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ImageAssetGetOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetGetOutputVariant2Delivery = TypedDict('ImageAssetGetOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ImageAssetGetOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[ImageAssetGetOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ImageAssetGetOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ImageAssetGetOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetGetOutputVariant2RecoveryOperation = TypedDict('ImageAssetGetOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ImageAssetGetOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetGetOutputVariant2Recovery = TypedDict('ImageAssetGetOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ImageAssetGetOutputVariant2RecoveryOperation],
})
ImageAssetGetOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ImageAssetGetOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ImageAssetGetOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ImageAssetGetOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ImageAssetGetOutput).
ImageAssetGetOutput = Union[ImageAssetGetOutputVariant2, ImageAssetGetOutputVariant1]

_ImageAssetGetInputAdapter = TypeAdapter(ImageAssetGetInput)
_ImageAssetGetOutputAdapter = TypeAdapter(ImageAssetGetOutput)