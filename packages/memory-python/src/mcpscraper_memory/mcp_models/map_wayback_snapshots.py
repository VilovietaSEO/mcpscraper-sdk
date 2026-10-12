from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class MapWaybackSnapshotsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    url: Annotated[str, Field(min_length=1)] = Field(..., alias='url', description='Original public page/site URL, domain, or a web.archive.org replay URL to inventory.')
    scope: Union[Literal['exact', 'prefix', 'host', 'domain'], None] = Field(None, alias='scope', description='exact = one page; prefix = one path tree; host = one hostname; domain = the domain plus subdomains. Ignored when urls is provided.')
    urls: Union[Annotated[list[str], Field(min_length=1, max_length=100)], None] = Field(None, alias='urls', description='Optional selected page URLs to inventory together using exact matching. Every URL must belong to the same site as url.')
    from_: Union[str, None] = Field(None, alias='from', description='Inclusive beginning of the archive range: YYYY, YYYY-MM, YYYY-MM-DD, or a 14-digit Wayback timestamp.')
    to: Union[str, None] = Field(None, alias='to', description='Inclusive end of the archive range: YYYY, YYYY-MM, YYYY-MM-DD, or a 14-digit Wayback timestamp.')
    successful_html_only: Union[bool, None] = Field(None, alias='successfulHtmlOnly', description='Count only HTTP 200 text/html captures. Set false to include redirects, errors, and archived assets.')
    max_captures: Union[Annotated[int, Field(ge=1, le=100000)], None] = Field(None, alias='maxCaptures', description='Maximum CDX capture rows to scan. If reached, countType is lower_bound instead of exact. Narrow the range or raise this cap for an exact large inventory.')
    include_captures: Union[bool, None] = Field(None, alias='includeCaptures', description='Return individual timestamp rows in addition to aggregate counts. Leave false for a compact count-only inventory.')
    max_capture_rows: Union[Annotated[int, Field(ge=0, le=1000)], None] = Field(None, alias='maxCaptureRows', description='Maximum individual capture rows returned when includeCaptures is true. Aggregated counts still use every scanned capture.')
    delivery: Union[Literal['auto', 'inline', 'artifact'], None] = Field(None, alias='delivery', description='auto returns bounded results and offloads large inventories; inline still offloads above the hard context limit; artifact always creates an owner-scoped report artifact.')


MapWaybackSnapshotsOutputVariant1FirstCaptureVariant1 = TypedDict('MapWaybackSnapshotsOutputVariant1FirstCaptureVariant1', {
    'timestamp': Required[str],
    'originalUrl': Required[str],
    'digest': Required[Union[str, None]],
    'rawReplayUrl': Required[str],
    'replayUrl': Required[Union[str, None]],
    'statusCode': NotRequired[Union[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)], None]],
    'mimeType': NotRequired[Union[str, None]],
    'length': NotRequired[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
})
MapWaybackSnapshotsOutputVariant1FirstCaptureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapWaybackSnapshotsOutputVariant1LastCaptureVariant1 = TypedDict('MapWaybackSnapshotsOutputVariant1LastCaptureVariant1', {
    'timestamp': Required[str],
    'originalUrl': Required[str],
    'digest': Required[Union[str, None]],
    'rawReplayUrl': Required[str],
    'replayUrl': Required[Union[str, None]],
    'statusCode': NotRequired[Union[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)], None]],
    'mimeType': NotRequired[Union[str, None]],
    'length': NotRequired[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
})
MapWaybackSnapshotsOutputVariant1LastCaptureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapWaybackSnapshotsOutputVariant1MonthlyCountsItem = TypedDict('MapWaybackSnapshotsOutputVariant1MonthlyCountsItem', {
    'month': Required[str],
    'captures': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
MapWaybackSnapshotsOutputVariant1MonthlyCountsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapWaybackSnapshotsOutputVariant1YearlyCountsItem = TypedDict('MapWaybackSnapshotsOutputVariant1YearlyCountsItem', {
    'year': Required[str],
    'captures': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
MapWaybackSnapshotsOutputVariant1YearlyCountsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapWaybackSnapshotsOutputVariant1PerUrlItem = TypedDict('MapWaybackSnapshotsOutputVariant1PerUrlItem', {
    'url': Required[str],
    'captures': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'uniqueDigests': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'firstTimestamp': Required[str],
    'lastTimestamp': Required[str],
})
MapWaybackSnapshotsOutputVariant1PerUrlItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapWaybackSnapshotsOutputVariant1CapturesItem = TypedDict('MapWaybackSnapshotsOutputVariant1CapturesItem', {
    'timestamp': Required[str],
    'originalUrl': Required[str],
    'digest': Required[Union[str, None]],
    'rawReplayUrl': Required[str],
    'replayUrl': Required[Union[str, None]],
    'statusCode': NotRequired[Union[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)], None]],
    'mimeType': NotRequired[Union[str, None]],
    'length': NotRequired[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
})
MapWaybackSnapshotsOutputVariant1CapturesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapWaybackSnapshotsOutputVariant1Artifact = TypedDict('MapWaybackSnapshotsOutputVariant1Artifact', {
    'artifactId': Required[str],
    'bytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'expiresAt': Required[str],
    'preview': Required[str],
})
MapWaybackSnapshotsOutputVariant1Artifact.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapWaybackSnapshotsOutputVariant1Delivery = TypedDict('MapWaybackSnapshotsOutputVariant1Delivery', {
    'requested': Required[Literal['auto', 'inline', 'artifact']],
    'effective': Required[Literal['inline', 'artifact']],
    'retained': Required[bool],
    'nextAction': Required[Union[str, None]],
})
MapWaybackSnapshotsOutputVariant1Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MapWaybackSnapshotsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    url: str = Field(..., alias='url', description='')
    scope: Literal['exact', 'prefix', 'host', 'domain'] = Field(..., alias='scope', description='')
    selected_urls: Union[list[str], None] = Field(..., alias='selectedUrls', description='')
    from_: Union[str, None] = Field(..., alias='from', description='')
    to: Union[str, None] = Field(..., alias='to', description='')
    successful_html_only: bool = Field(..., alias='successfulHtmlOnly', description='')
    total_captures: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='totalCaptures', description='')
    count_type: Literal['exact', 'lower_bound'] = Field(..., alias='countType', description='')
    complete: bool = Field(..., alias='complete', description='')
    truncated: bool = Field(..., alias='truncated', description='')
    max_captures: Annotated[int, Field(ge=1, le=9007199254740991)] = Field(..., alias='maxCaptures', description='')
    query_pages: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='queryPages', description='')
    unique_urls: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='uniqueUrls', description='')
    unique_digests: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='uniqueDigests', description='')
    first_capture: Union[MapWaybackSnapshotsOutputVariant1FirstCaptureVariant1, None] = Field(..., alias='firstCapture', description='')
    last_capture: Union[MapWaybackSnapshotsOutputVariant1LastCaptureVariant1, None] = Field(..., alias='lastCapture', description='')
    monthly_counts: list[MapWaybackSnapshotsOutputVariant1MonthlyCountsItem] = Field(..., alias='monthlyCounts', description='')
    yearly_counts: list[MapWaybackSnapshotsOutputVariant1YearlyCountsItem] = Field(..., alias='yearlyCounts', description='')
    missing_months: list[str] = Field(..., alias='missingMonths', description='')
    per_url: list[MapWaybackSnapshotsOutputVariant1PerUrlItem] = Field(..., alias='perUrl', description='')
    per_url_truncated_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='perUrlTruncatedCount', description='')
    captures: list[MapWaybackSnapshotsOutputVariant1CapturesItem] = Field(..., alias='captures', description='')
    capture_rows_truncated_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='captureRowsTruncatedCount', description='')
    duration_ms: Annotated[Union[float, int], Field(ge=0)] = Field(..., alias='durationMs', description='')
    truncated_count: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='truncatedCount', description='')
    artifact: Union[MapWaybackSnapshotsOutputVariant1Artifact, None] = Field(None, alias='artifact', description='')
    delivery: MapWaybackSnapshotsOutputVariant1Delivery = Field(..., alias='delivery', description='')


MapWaybackSnapshotsOutputVariant2DeliveryArtifactsItem = TypedDict('MapWaybackSnapshotsOutputVariant2DeliveryArtifactsItem', {
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
MapWaybackSnapshotsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapWaybackSnapshotsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('MapWaybackSnapshotsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
MapWaybackSnapshotsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapWaybackSnapshotsOutputVariant2Delivery = TypedDict('MapWaybackSnapshotsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[MapWaybackSnapshotsOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[MapWaybackSnapshotsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
MapWaybackSnapshotsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapWaybackSnapshotsOutputVariant2RecoveryOperation = TypedDict('MapWaybackSnapshotsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
MapWaybackSnapshotsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapWaybackSnapshotsOutputVariant2Recovery = TypedDict('MapWaybackSnapshotsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[MapWaybackSnapshotsOutputVariant2RecoveryOperation],
})
MapWaybackSnapshotsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MapWaybackSnapshotsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: MapWaybackSnapshotsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: MapWaybackSnapshotsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(MapWaybackSnapshotsOutput).
MapWaybackSnapshotsOutput = Union[MapWaybackSnapshotsOutputVariant1, MapWaybackSnapshotsOutputVariant2]

_MapWaybackSnapshotsInputAdapter = TypeAdapter(MapWaybackSnapshotsInput)
_MapWaybackSnapshotsOutputAdapter = TypeAdapter(MapWaybackSnapshotsOutput)