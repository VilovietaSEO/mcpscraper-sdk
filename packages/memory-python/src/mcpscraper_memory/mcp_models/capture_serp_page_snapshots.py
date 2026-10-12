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


class CaptureSerpPageSnapshotsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    schema_version: Literal['serp-intelligence.page-snapshots.v1'] = Field(..., alias='schemaVersion', description='')
    status: str = Field(..., alias='status', description='')
    count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='count', description='')
    captured_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='capturedCount', description='')
    failed_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='failedCount', description='')
    skipped_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='skippedCount', description='')
    captures: list[dict[str, Any]] = Field(..., alias='captures', description='')
    resolved_inputs: dict[str, Any] = Field(..., alias='resolvedInputs', description='')
    diagnostics: Union[dict[str, Any], None] = Field(..., alias='diagnostics', description='')
    provider_payload: dict[str, Any] = Field(..., alias='providerPayload', description='')


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