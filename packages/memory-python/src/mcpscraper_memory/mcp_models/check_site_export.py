from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CheckSiteExportInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    job_id: Annotated[str, Field(min_length=1)] = Field(..., alias='jobId', description='The jobId returned by extract_site, analyze_site_similarity, or audit_site. Poll until status is complete, partial, or failed; partial jobs still return successful content and failure details.')


class CheckSiteExportOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    job_id: str = Field(..., alias='jobId', description='')
    status: Literal['pending', 'running', 'complete', 'partial', 'failed'] = Field(..., alias='status', description='')
    start_url: Union[str, None] = Field(None, alias='startUrl', description='')
    total_urls: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='totalUrls', description='')
    done_urls: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='doneUrls', description='')
    discovered: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='discovered', description='')
    attempted: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='attempted', description='')
    successful: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='successful', description='')
    failed: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='failed', description='')
    remaining: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='remaining', description='')
    requested_max_pages: Union[Annotated[int, Field(ge=1, le=9007199254740991)], None] = Field(None, alias='requestedMaxPages', description='Page cap requested by the caller.')
    effective_max_pages: Union[Annotated[int, Field(ge=1, le=9007199254740991)], None] = Field(None, alias='effectiveMaxPages', description='Page cap funded by the available credit hold.')
    credit_limited: Union[bool, None] = Field(None, alias='creditLimited', description='True when available credits reduced the requested page cap.')
    credit_truncated: Union[bool, None] = Field(None, alias='creditTruncated', description='True when the crawl reached the reduced funded cap and may have omitted discoverable pages.')
    bundle_url: Union[str, None] = Field(..., alias='bundleUrl', description='Downloadable ZIP URL for a terminal complete, partial, or diagnostic failed export; null while unavailable.')
    artifact_id: Union[Union[str, None], None] = Field(None, alias='artifactId', description='Owner-scoped artifact ID for archive_read. Prefer this over the temporary bundle URL.')
    bundle_bytes: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(..., alias='bundleBytes', description='ZIP size in bytes when a bundle is available; null otherwise.')
    bundle_expires_at: Union[Union[str, None], None] = Field(None, alias='bundleExpiresAt', description='Artifact retention expiry when the hosted bundle is private.')
    bundle_url_expires_at: Union[Union[str, None], None] = Field(None, alias='bundleUrlExpiresAt', description='Signed download URL expiry when applicable.')
    error: Union[Union[str, None], None] = Field(None, alias='error', description='Terminal error or partial-delivery explanation, when present.')
    error_code: Union[str, None] = Field(None, alias='error_code', description='')
    error_type: Union[str, None] = Field(None, alias='error_type', description='')
    retryable: Union[bool, None] = Field(None, alias='retryable', description='')
    retry_after_seconds: Union[Annotated[int, Field(ge=1, le=9007199254740991)], None] = Field(None, alias='retry_after_seconds', description='')
    charge_status: Union[Literal['not_charged', 'refund_pending', 'refunded', 'charged'], None] = Field(None, alias='charge_status', description='')
    next_actions: Union[dict[str, Any], None] = Field(None, alias='nextActions', description='Machine-readable next tool calls for polling, direct page reads, image reads, and human download.')
    updated_at: Union[str, None] = Field(None, alias='updatedAt', description='')
    local_path: Union[Union[str, None], None] = Field(None, alias='localPath', description='Server-generated path when an installed stdio server mirrored the ZIP under MCP_SCRAPER_OUTPUT_DIR.')
    local_mirror_error: Union[Union[str, None], None] = Field(None, alias='localMirrorError', description='Why optional local mirroring failed; the owner-scoped artifact remains available.')


CheckSiteExportOutputVariant2DeliveryArtifactsItem = TypedDict('CheckSiteExportOutputVariant2DeliveryArtifactsItem', {
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
CheckSiteExportOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CheckSiteExportOutputVariant2DeliveryAvailableExportsItem = TypedDict('CheckSiteExportOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CheckSiteExportOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CheckSiteExportOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CheckSiteExportOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CheckSiteExportOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CheckSiteExportOutputVariant2Delivery = TypedDict('CheckSiteExportOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CheckSiteExportOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CheckSiteExportOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CheckSiteExportOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CheckSiteExportOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CheckSiteExportOutputVariant2RecoveryOperation = TypedDict('CheckSiteExportOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CheckSiteExportOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CheckSiteExportOutputVariant2Recovery = TypedDict('CheckSiteExportOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CheckSiteExportOutputVariant2RecoveryOperation],
})
CheckSiteExportOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CheckSiteExportOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CheckSiteExportOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CheckSiteExportOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CheckSiteExportOutput).
CheckSiteExportOutput = Union[CheckSiteExportOutputVariant1, CheckSiteExportOutputVariant2]

_CheckSiteExportInputAdapter = TypeAdapter(CheckSiteExportInput)
_CheckSiteExportOutputAdapter = TypeAdapter(CheckSiteExportOutput)