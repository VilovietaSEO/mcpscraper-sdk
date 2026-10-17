from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ExtractUrlInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    url: str = Field(..., alias='url', description='Public http/https URL to extract.')
    screenshot: Union[bool, None] = Field(None, alias='screenshot', description='Capture a full-page screenshot. Large captures may be offloaded to an owned artifact.')
    screenshot_device: Union[Literal['desktop', 'mobile'], None] = Field(None, alias='screenshotDevice', description='Viewport: desktop = 1440×900, mobile = 390×844.')
    extract_branding: Union[bool, None] = Field(None, alias='extractBranding', description='Extract brand colors, fonts, logo, and favicon via a rendered session.')
    include_featured_image: Union[bool, None] = Field(None, alias='includeFeaturedImage', description='Return the best featured image from Open Graph, Twitter, JSON-LD, or page content. Wayback URLs get the timestamp-matched archived image.')
    download_media: Union[bool, None] = Field(None, alias='downloadMedia', description='Deprecated alias for preserveMedia; omit when using preserveMedia.')
    media_types: Union[list[Literal['image', 'video', 'audio']], None] = Field(None, alias='mediaTypes', description='Media types to download. Default all three.')
    max_media_assets: Union[Annotated[int, Field(ge=1, le=250)], None] = Field(None, alias='maxMediaAssets', description='Maximum media records to retain after filtering and variant collapse.')
    max_inline_images: Union[Annotated[int, Field(ge=0, le=5)], None] = Field(None, alias='maxInlineImages', description='Maximum images attached as AI-readable content blocks. All downloaded media stays available in the ZIP.')
    delivery: Union[Literal['auto', 'inline', 'artifact', 'memory'], None] = Field(None, alias='delivery', description='auto offloads large results; artifact always returns an artifact; memory stores in hosted Memory; inline is bounded.')
    preserve_media: Union[bool, None] = Field(None, alias='preserveMedia', description='Collect media from static plus rendered page content, collapse responsive variants, attach bounded previews, and create an owner-scoped ZIP readable with archive_read.')
    deposit_to_vault: Union[bool, None] = Field(None, alias='depositToVault', description="Save the full page content into the user's MCP Memory vault, embedded for semantic recall — the full body is NOT returned to chat.")
    vault_name: Union[Annotated[str, Field(min_length=1, max_length=120)], None] = Field(None, alias='vaultName', description='Optional vault to deposit into; defaults to the personal vault.')
    idempotency_key: Union[Annotated[str, Field(min_length=8, max_length=200)], None] = Field(None, alias='idempotencyKey', description='Retry key: reuse after a timeout to avoid re-billing. New key per extraction.')


class ExtractUrlOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    job_id: str = Field(..., alias='jobId', description='')
    status: Literal['pending', 'running', 'done', 'failed', 'cancelled'] = Field(..., alias='status', description='')
    status_tool: Literal['extract_url_status'] = Field(..., alias='statusTool', description='')
    replayed: bool = Field(..., alias='replayed', description='')


ExtractUrlOutputVariant2DeliveryArtifactsItem = TypedDict('ExtractUrlOutputVariant2DeliveryArtifactsItem', {
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
ExtractUrlOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlOutputVariant2DeliveryAvailableExportsItem = TypedDict('ExtractUrlOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
ExtractUrlOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ExtractUrlOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ExtractUrlOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlOutputVariant2Delivery = TypedDict('ExtractUrlOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ExtractUrlOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[ExtractUrlOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ExtractUrlOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ExtractUrlOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlOutputVariant2RecoveryOperation = TypedDict('ExtractUrlOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ExtractUrlOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractUrlOutputVariant2Recovery = TypedDict('ExtractUrlOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ExtractUrlOutputVariant2RecoveryOperation],
})
ExtractUrlOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ExtractUrlOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ExtractUrlOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ExtractUrlOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ExtractUrlOutput).
ExtractUrlOutput = Union[ExtractUrlOutputVariant1, ExtractUrlOutputVariant2]

_ExtractUrlInputAdapter = TypeAdapter(ExtractUrlInput)
_ExtractUrlOutputAdapter = TypeAdapter(ExtractUrlOutput)