from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ImageAssetMoveInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Union[str, None] = Field(None, alias='vault', description='Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.')
    asset_id: Annotated[str, Field(min_length=1)] = Field(..., alias='assetId', description='Opaque image asset identifier returned by an image asset tool.')
    project_id: Union[Union[Annotated[str, Field(min_length=1)], None], None] = Field(None, alias='projectId', description='Opaque image project identifier returned by an image project tool.')
    folder_id: Union[Union[Annotated[str, Field(min_length=1)], None], None] = Field(None, alias='folderId', description='Opaque image folder identifier; omit only when the project root is intended.')


ImageAssetMoveOutputVariant1AssetPreview = TypedDict('ImageAssetMoveOutputVariant1AssetPreview', {
    'url': Required[str],
    'expiresAt': Required[str],
    'mimeType': Required[Literal['image/webp']],
})
ImageAssetMoveOutputVariant1AssetPreview.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetMoveOutputVariant1Asset = TypedDict('ImageAssetMoveOutputVariant1Asset', {
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
    'preview': NotRequired[ImageAssetMoveOutputVariant1AssetPreview],
})
ImageAssetMoveOutputVariant1Asset.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ImageAssetMoveOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    asset: Union[ImageAssetMoveOutputVariant1Asset, None] = Field(None, alias='asset', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


ImageAssetMoveOutputVariant2DeliveryArtifactsItem = TypedDict('ImageAssetMoveOutputVariant2DeliveryArtifactsItem', {
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
ImageAssetMoveOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetMoveOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ImageAssetMoveOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ImageAssetMoveOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetMoveOutputVariant2Delivery = TypedDict('ImageAssetMoveOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ImageAssetMoveOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ImageAssetMoveOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ImageAssetMoveOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetMoveOutputVariant2RecoveryOperation = TypedDict('ImageAssetMoveOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ImageAssetMoveOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetMoveOutputVariant2Recovery = TypedDict('ImageAssetMoveOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ImageAssetMoveOutputVariant2RecoveryOperation],
})
ImageAssetMoveOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ImageAssetMoveOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ImageAssetMoveOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ImageAssetMoveOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ImageAssetMoveOutput).
ImageAssetMoveOutput = Union[ImageAssetMoveOutputVariant2, ImageAssetMoveOutputVariant1]

_ImageAssetMoveInputAdapter = TypeAdapter(ImageAssetMoveInput)
_ImageAssetMoveOutputAdapter = TypeAdapter(ImageAssetMoveOutput)