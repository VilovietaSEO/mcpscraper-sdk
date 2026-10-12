from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


CaptureSerpPageSnapshotsInputTargetsItem = TypedDict('CaptureSerpPageSnapshotsInputTargetsItem', {
    'url': Required[str],
    'sourceKind': NotRequired[Literal['organic', 'ai_citation', 'local_pack_website', 'configured_target', 'site_subject']],
    'sourcePosition': NotRequired[Annotated[int, Field(ge=1, le=9007199254740991)]],
})
CaptureSerpPageSnapshotsInputTargetsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class CaptureSerpPageSnapshotsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    urls: Union[Annotated[list[str], Field(min_length=1, max_length=25)], None] = Field(None, alias='urls', description='Public HTTP/HTTPS URLs to capture. Provide exactly one of urls or targets. Do not pass localhost, private IPs, file URLs, or internal admin URLs.')
    targets: Union[Annotated[list[CaptureSerpPageSnapshotsInputTargetsItem], Field(min_length=1, max_length=25)], None] = Field(None, alias='targets', description='Structured targets. Provide exactly one of targets or urls; use targets when source kind or position should be preserved.')
    max_concurrency: Union[Annotated[int, Field(ge=1, le=5)], None] = Field(None, alias='maxConcurrency', description='Parallel page captures.')
    timeout_ms: Union[Annotated[int, Field(ge=1000, le=60000)], None] = Field(None, alias='timeoutMs', description='Per-page capture timeout in milliseconds; timeouts return as structured capture failures.')


CaptureSerpPageSnapshotsOutputVariant1CapturesItemHeadingsItem = TypedDict('CaptureSerpPageSnapshotsOutputVariant1CapturesItemHeadingsItem', {
    'level': Required[Annotated[int, Field(ge=1, le=6)]],
    'text': Required[str],
})
CaptureSerpPageSnapshotsOutputVariant1CapturesItemHeadingsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpPageSnapshotsOutputVariant1CapturesItemArtifact = TypedDict('CaptureSerpPageSnapshotsOutputVariant1CapturesItemArtifact', {
    'htmlBlobUrl': NotRequired[Union[str, None]],
    'textBlobUrl': NotRequired[Union[str, None]],
    'markdownBlobUrl': NotRequired[Union[str, None]],
    'screenshotBlobUrl': NotRequired[Union[str, None]],
    'contentSha256': NotRequired[Union[str, None]],
    'capturedAt': NotRequired[Union[str, None]],
})
CaptureSerpPageSnapshotsOutputVariant1CapturesItemArtifact.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpPageSnapshotsOutputVariant1CapturesItemErrorVariant1 = TypedDict('CaptureSerpPageSnapshotsOutputVariant1CapturesItemErrorVariant1', {
    'code': Required[Literal['invalid_url', 'timeout', 'capture_failed']],
    'message': Required[str],
})
CaptureSerpPageSnapshotsOutputVariant1CapturesItemErrorVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpPageSnapshotsOutputVariant1CapturesItemLinkCounts = TypedDict('CaptureSerpPageSnapshotsOutputVariant1CapturesItemLinkCounts', {
    'wordCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'internalLinkCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'externalLinkCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'totalLinkCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
CaptureSerpPageSnapshotsOutputVariant1CapturesItemLinkCounts.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpPageSnapshotsOutputVariant1CapturesItemHashes = TypedDict('CaptureSerpPageSnapshotsOutputVariant1CapturesItemHashes', {
    'htmlSha256': Required[Union[str, None]],
    'markdownSha256': Required[Union[str, None]],
    'textSha256': Required[Union[str, None]],
})
CaptureSerpPageSnapshotsOutputVariant1CapturesItemHashes.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpPageSnapshotsOutputVariant1CapturesItemContent = TypedDict('CaptureSerpPageSnapshotsOutputVariant1CapturesItemContent', {
    'html': Required[Union[str, None]],
    'markdown': Required[Union[str, None]],
    'text': Required[Union[str, None]],
})
CaptureSerpPageSnapshotsOutputVariant1CapturesItemContent.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpPageSnapshotsOutputVariant1CapturesItemDiagnosticsUrlValidation = TypedDict('CaptureSerpPageSnapshotsOutputVariant1CapturesItemDiagnosticsUrlValidation', {
    'passed': Required[bool],
})
CaptureSerpPageSnapshotsOutputVariant1CapturesItemDiagnosticsUrlValidation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpPageSnapshotsOutputVariant1CapturesItemDiagnosticsBrowserFallback = TypedDict('CaptureSerpPageSnapshotsOutputVariant1CapturesItemDiagnosticsBrowserFallback', {
    'configured': Required[bool],
    'used': Required[bool],
    'boundedByTimeoutMs': Required[Annotated[Union[float, int], Field(ge=0)]],
})
CaptureSerpPageSnapshotsOutputVariant1CapturesItemDiagnosticsBrowserFallback.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpPageSnapshotsOutputVariant1CapturesItemDiagnosticsContent = TypedDict('CaptureSerpPageSnapshotsOutputVariant1CapturesItemDiagnosticsContent', {
    'htmlIncluded': Required[bool],
    'markdownIncluded': Required[bool],
    'textIncluded': Required[bool],
    'maxContentChars': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'truncated': Required[bool],
})
CaptureSerpPageSnapshotsOutputVariant1CapturesItemDiagnosticsContent.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpPageSnapshotsOutputVariant1CapturesItemDiagnostics = TypedDict('CaptureSerpPageSnapshotsOutputVariant1CapturesItemDiagnostics', {
    'requestedAt': Required[str],
    'completedAt': Required[str],
    'durationMs': Required[Annotated[Union[float, int], Field(ge=0)]],
    'urlValidation': Required[CaptureSerpPageSnapshotsOutputVariant1CapturesItemDiagnosticsUrlValidation],
    'browserFallback': Required[CaptureSerpPageSnapshotsOutputVariant1CapturesItemDiagnosticsBrowserFallback],
    'content': Required[CaptureSerpPageSnapshotsOutputVariant1CapturesItemDiagnosticsContent],
})
CaptureSerpPageSnapshotsOutputVariant1CapturesItemDiagnostics.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpPageSnapshotsOutputVariant1CapturesItem = TypedDict('CaptureSerpPageSnapshotsOutputVariant1CapturesItem', {
    'url': NotRequired[str],
    'requestedUrl': NotRequired[str],
    'finalUrl': NotRequired[Union[str, None]],
    'sourceKind': NotRequired[Literal['organic', 'ai_citation', 'local_pack_website', 'configured_target', 'site_subject']],
    'sourcePosition': NotRequired[Union[Annotated[int, Field(ge=1, le=9007199254740991)], None]],
    'status': NotRequired[Literal['captured', 'skipped', 'failed']],
    'fetchedVia': NotRequired[Union[Literal['fetch', 'headless', 'browser', 'mcp'], None]],
    'httpStatus': NotRequired[Union[Annotated[int, Field(ge=100, le=599)], None]],
    'contentType': NotRequired[Union[str, None]],
    'title': NotRequired[Union[str, None]],
    'canonicalUrl': NotRequired[Union[str, None]],
    'metaDescription': NotRequired[Union[str, None]],
    'headings': NotRequired[list[CaptureSerpPageSnapshotsOutputVariant1CapturesItemHeadingsItem]],
    'artifact': NotRequired[CaptureSerpPageSnapshotsOutputVariant1CapturesItemArtifact],
    'error': NotRequired[Union[CaptureSerpPageSnapshotsOutputVariant1CapturesItemErrorVariant1, None]],
    'schemaTypes': NotRequired[list[str]],
    'wordCount': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'linkCounts': NotRequired[CaptureSerpPageSnapshotsOutputVariant1CapturesItemLinkCounts],
    'hashes': NotRequired[CaptureSerpPageSnapshotsOutputVariant1CapturesItemHashes],
    'content': NotRequired[CaptureSerpPageSnapshotsOutputVariant1CapturesItemContent],
    'diagnostics': NotRequired[CaptureSerpPageSnapshotsOutputVariant1CapturesItemDiagnostics],
})
CaptureSerpPageSnapshotsOutputVariant1CapturesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpPageSnapshotsOutputVariant1DiagnosticsVariant1 = TypedDict('CaptureSerpPageSnapshotsOutputVariant1DiagnosticsVariant1', {
    'requestedCount': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'capturedCount': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'failedCount': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'maxConcurrency': NotRequired[Annotated[int, Field(ge=1, le=5)]],
    'timeoutMs': NotRequired[Annotated[Union[float, int], Field(ge=0)]],
})
CaptureSerpPageSnapshotsOutputVariant1DiagnosticsVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CaptureSerpPageSnapshotsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    schema_version: Literal['serp-intelligence.page-snapshots.v1'] = Field(..., alias='schemaVersion', description='')
    status: str = Field(..., alias='status', description='')
    count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='count', description='')
    captured_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='capturedCount', description='')
    failed_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='failedCount', description='')
    skipped_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='skippedCount', description='')
    captures: list[CaptureSerpPageSnapshotsOutputVariant1CapturesItem] = Field(..., alias='captures', description='')
    resolved_inputs: dict[str, Any] = Field(..., alias='resolvedInputs', description='')
    diagnostics: Union[CaptureSerpPageSnapshotsOutputVariant1DiagnosticsVariant1, None] = Field(..., alias='diagnostics', description='')


CaptureSerpPageSnapshotsOutputVariant2DeliveryArtifactsItem = TypedDict('CaptureSerpPageSnapshotsOutputVariant2DeliveryArtifactsItem', {
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
CaptureSerpPageSnapshotsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpPageSnapshotsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CaptureSerpPageSnapshotsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CaptureSerpPageSnapshotsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpPageSnapshotsOutputVariant2Delivery = TypedDict('CaptureSerpPageSnapshotsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CaptureSerpPageSnapshotsOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CaptureSerpPageSnapshotsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CaptureSerpPageSnapshotsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpPageSnapshotsOutputVariant2RecoveryOperation = TypedDict('CaptureSerpPageSnapshotsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CaptureSerpPageSnapshotsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpPageSnapshotsOutputVariant2Recovery = TypedDict('CaptureSerpPageSnapshotsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CaptureSerpPageSnapshotsOutputVariant2RecoveryOperation],
})
CaptureSerpPageSnapshotsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CaptureSerpPageSnapshotsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CaptureSerpPageSnapshotsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CaptureSerpPageSnapshotsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CaptureSerpPageSnapshotsOutput).
CaptureSerpPageSnapshotsOutput = Union[CaptureSerpPageSnapshotsOutputVariant1, CaptureSerpPageSnapshotsOutputVariant2]

_CaptureSerpPageSnapshotsInputAdapter = TypeAdapter(CaptureSerpPageSnapshotsInput)
_CaptureSerpPageSnapshotsOutputAdapter = TypeAdapter(CaptureSerpPageSnapshotsOutput)