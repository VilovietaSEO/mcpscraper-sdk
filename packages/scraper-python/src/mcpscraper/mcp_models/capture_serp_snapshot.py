from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CaptureSerpSnapshotInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    query: Annotated[str, Field(min_length=1)] = Field(..., alias='query', description='Search topic to capture, exactly as it should be searched. Include the place here when you want it in the search terms — the server sends your query to Google unchanged and never adds or removes a location.')
    location: Union[str, None] = Field(None, alias='location', description='Where Google should think the searcher is. Sets the Google UULE parameter only — it never changes your query text and never selects a proxy. To put the place in the search terms too, write it into query.')
    gl: Union[Annotated[str, Field(min_length=2, max_length=2)], None] = Field(None, alias='gl', description='Google country code inferred from the requested market.')
    hl: Union[str, None] = Field(None, alias='hl', description='Google interface/content language inferred from the user request.')
    device: Union[Literal['desktop', 'mobile'], None] = Field(None, alias='device', description='SERP device context. Use mobile only for mobile rankings/evidence.')
    pages: Union[Annotated[int, Field(ge=1, le=2)], None] = Field(None, alias='pages', description='Google result pages to capture. Use 2 only for deeper ranking evidence.')
    include_page_snapshots: Union[bool, None] = Field(None, alias='includePageSnapshots', description='Also capture ranking-page snapshots for selected SERP URLs. Each attempted snapshot adds 1 Credit.')
    page_snapshot_limit: Union[Annotated[int, Field(ge=0, le=10)], None] = Field(None, alias='pageSnapshotLimit', description='Maximum ranking-page snapshots when includePageSnapshots is true. This capacity is held up front and unused capacity is refunded.')


CaptureSerpSnapshotOutputVariant1BillingVariant1 = TypedDict('CaptureSerpSnapshotOutputVariant1BillingVariant1', {
    'creditsUsed': Required[Union[Annotated[Union[float, int], Field(ge=0)], None]],
    'requestId': Required[Union[str, None]],
    'jobId': Required[Union[str, None]],
})
CaptureSerpSnapshotOutputVariant1BillingVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CaptureSerpSnapshotOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    schema_version: Literal['serp-intelligence.capture.v1'] = Field(..., alias='schemaVersion', description='')
    status: str = Field(..., alias='status', description='')
    query: Union[str, None] = Field(..., alias='query', description='')
    location: Union[str, None] = Field(..., alias='location', description='')
    captured_at: Union[str, None] = Field(..., alias='capturedAt', description='')
    result_count: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(..., alias='resultCount', description='')
    organic_result_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='organicResultCount', description='')
    local_pack_result_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='localPackResultCount', description='')
    page_snapshot_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='pageSnapshotCount', description='')
    page_snapshot_failed_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='pageSnapshotFailedCount', description='')
    snapshot_id: Union[str, None] = Field(..., alias='snapshotId', description='')
    resolved_inputs: dict[str, Any] = Field(..., alias='resolvedInputs', description='')
    artifacts: list[dict[str, Any]] = Field(..., alias='artifacts', description='')
    billing: Union[CaptureSerpSnapshotOutputVariant1BillingVariant1, None] = Field(..., alias='billing', description='')
    diagnostics: Union[dict[str, Any], None] = Field(..., alias='diagnostics', description='')
    provider_payload: dict[str, Any] = Field(..., alias='providerPayload', description='')


CaptureSerpSnapshotOutputVariant2DeliveryArtifactsItem = TypedDict('CaptureSerpSnapshotOutputVariant2DeliveryArtifactsItem', {
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
CaptureSerpSnapshotOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CaptureSerpSnapshotOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CaptureSerpSnapshotOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant2Delivery = TypedDict('CaptureSerpSnapshotOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CaptureSerpSnapshotOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CaptureSerpSnapshotOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CaptureSerpSnapshotOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant2RecoveryOperation = TypedDict('CaptureSerpSnapshotOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CaptureSerpSnapshotOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CaptureSerpSnapshotOutputVariant2Recovery = TypedDict('CaptureSerpSnapshotOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CaptureSerpSnapshotOutputVariant2RecoveryOperation],
})
CaptureSerpSnapshotOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CaptureSerpSnapshotOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CaptureSerpSnapshotOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CaptureSerpSnapshotOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CaptureSerpSnapshotOutput).
CaptureSerpSnapshotOutput = Union[CaptureSerpSnapshotOutputVariant1, CaptureSerpSnapshotOutputVariant2]

_CaptureSerpSnapshotInputAdapter = TypeAdapter(CaptureSerpSnapshotInput)
_CaptureSerpSnapshotOutputAdapter = TypeAdapter(CaptureSerpSnapshotOutput)