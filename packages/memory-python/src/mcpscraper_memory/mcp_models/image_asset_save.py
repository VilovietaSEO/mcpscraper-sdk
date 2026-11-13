from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ImageAssetSaveInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Union[str, None] = Field(None, alias='vault', description='Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.')
    project_id: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='projectId', description='Opaque image project identifier returned by an image project tool.')
    folder_id: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='folderId', description='Opaque image folder identifier; omit only when the project root is intended.')
    source_url: Union[str, None] = Field(None, alias='sourceUrl', description='Public HTTPS image URL. Private-network and redirect targets are rejected.')
    artifact_id: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='artifactId', description='Owned MCP Scraper artifact ID. Available through the aggregate MCP handoff.')
    image_base64: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='imageBase64', description='Bounded base64 image for clients without an upload transport; maximum decoded size is 20 MiB.')
    title: Annotated[str, Field(min_length=1, max_length=240)] = Field(..., alias='title', description='Human-readable title for the proposed record or authored content.')
    description: Union[Annotated[str, Field(max_length=4000)], None] = Field(None, alias='description', description='Human-readable summary that distinguishes this record from similarly named records.')
    alt_text: Union[Annotated[str, Field(max_length=2000)], None] = Field(None, alias='altText', description='Concise accessible description of the image content and purpose.')
    tags: Union[Annotated[list[Annotated[str, Field(min_length=1, max_length=80)]], Field(max_length=20)], None] = Field(None, alias='tags', description='Canonical tag filter or tag set; use the appropriate vocabulary-listing tool before writing new tags.')
    source_ref: Union[dict[str, Union[Annotated[str, Field(max_length=1000)], Union[float, int], bool, None]], None] = Field(None, alias='sourceRef', description='Original source URL or opaque artifact reference preserved as image provenance.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Stable key for this logical save. Retrying the same request returns the same asset without another write.')


ImageAssetSaveOutputVariant1AssetPreview = TypedDict('ImageAssetSaveOutputVariant1AssetPreview', {
    'url': Required[str],
    'expiresAt': Required[str],
    'mimeType': Required[Literal['image/webp']],
})
ImageAssetSaveOutputVariant1AssetPreview.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetSaveOutputVariant1Asset = TypedDict('ImageAssetSaveOutputVariant1Asset', {
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
    'preview': NotRequired[ImageAssetSaveOutputVariant1AssetPreview],
})
ImageAssetSaveOutputVariant1Asset.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ImageAssetSaveOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    asset: Union[ImageAssetSaveOutputVariant1Asset, None] = Field(None, alias='asset', description='')
    reused_object: Union[bool, None] = Field(None, alias='reusedObject', description='')
    next_action: Union[str, None] = Field(None, alias='nextAction', description='')
    code: Union[str, None] = Field(None, alias='code', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


ImageAssetSaveOutputVariant2DeliveryArtifactsItem = TypedDict('ImageAssetSaveOutputVariant2DeliveryArtifactsItem', {
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
ImageAssetSaveOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetSaveOutputVariant2DeliveryAvailableExportsItem = TypedDict('ImageAssetSaveOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
ImageAssetSaveOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetSaveOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ImageAssetSaveOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ImageAssetSaveOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetSaveOutputVariant2Delivery = TypedDict('ImageAssetSaveOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ImageAssetSaveOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[ImageAssetSaveOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ImageAssetSaveOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ImageAssetSaveOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetSaveOutputVariant2RecoveryOperation = TypedDict('ImageAssetSaveOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ImageAssetSaveOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ImageAssetSaveOutputVariant2Recovery = TypedDict('ImageAssetSaveOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ImageAssetSaveOutputVariant2RecoveryOperation],
})
ImageAssetSaveOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ImageAssetSaveOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ImageAssetSaveOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ImageAssetSaveOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ImageAssetSaveOutput).
ImageAssetSaveOutput = Union[ImageAssetSaveOutputVariant2, ImageAssetSaveOutputVariant1]

_ImageAssetSaveInputAdapter = TypeAdapter(ImageAssetSaveInput)
_ImageAssetSaveOutputAdapter = TypeAdapter(ImageAssetSaveOutput)